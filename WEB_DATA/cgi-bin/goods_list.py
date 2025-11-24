import codecs
import os
import sqlite3
import sys
import urllib.parse

# 文字化け回避のため、標準出力をUTF-8に設定
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# HTMLから情報を取得
text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form = urllib.parse.parse_qs(text)
cate = form['cate'][0]
maker = form['maker'][0]
word = form.get('word',[''])[0] # フリーワードが空欄で'word'が存在しない場合は、指定したデフォルト値（ここでは空文字のリスト ['']）を返します。
user = form['user'][0]

# DBに接続
con = sqlite3.connect('kaden_web_cgi.db')
cur = con.cursor()

# DBより商品一覧取得
# カテゴリー：すべて、メーカー：すべて、フリーワード：空欄の場合
if cate =='すべて' and maker =='すべて'and word=='':
    cur.execute("SELECT name,goods_code,price FROM goods")
    row_list = cur.fetchall()
# カテゴリー：すべて、メーカー：すべて、フリーワード：空欄ではないの場合
elif cate == "すべて" and maker == "すべて" and word != '':
    cur.execute(f"SELECT name,goods_code,price FROM goods\
                WHERE name LIKE '%{word}%'OR goods_code LIKE '%{word}%'\
                OR desc LIKE '%{word}%' OR price LIKE '%{word}%'\
                OR goods_class LIKE '%{word}%' OR maker LIKE '%{word}%'")
    rows_list = cur.fetchall()
# カテゴリー：すべて、メーカー：すべて以外、フリーワード：空欄の場合
elif cate == "すべて" and maker != "すべて" and word != '':
    cur.execute(f"SELECT name,goods_code,price FROM goods WHERE maker='{maker}'")
    rows_list =cur.fetchall()
# カテゴリー：すべて、メーカー：すべて以外、フリーワード：空欄ではないの場合
elif cate == "すべて" and maker != "すべて" and word !="": 
    cur.execute(f"SELECT name,goods_code,price FROM goods WHERE maker='%{word}%'\
                AND( name LIKE '%{word}%' OR goods_code LIKE '%{word}%'OR desc LIKE '%{word}%'\
                OR price LIKE '%{word}%' OR goods_class LIKE '%{word}%'OR maker LIKE '%{word}%')")
    rows_list = cur.fetchall()

# カテゴリー：すべて以外、メーカー：すべて、フリーワード：空欄の場合
elif cate !='すべて' and maker =='すべて' and word =='':
    cur.execute(f"SELECT name,goods_code,price FROM goods WHERE goods_class ='{cate}'")
    rows_list=cur.fetchall()
# カテゴリー：すべて以外、メーカー：すべて、フリーワード：空欄ではないの場合
elif cate !='すべて' and maker =='すべて' and word !='':
    cur.execute(f"SELECT name,goods_code,price FROM goods WHERE goods_class='%{cate}%'\
                AND( name LIKE '%{word}%' OR goods_code LIKE '%{word}%'OR desc LIKE '%{word}%'\
                OR price LIKE '%{word}%' OR goods_class LIKE '%{word}%'OR maker LIKE '%{word}%')")
    rows_list = cur.fetchall()
# カテゴリー：すべて以外、メーカー：すべて以外、フリーワード：空欄ではないの場合
elif cate !='すべて' and maker !='すべて' and word !='':
    cur.execute(f"SELECT name,goods_code,price FROM goods WHERE goods_class='{cate}' AND maker ='{maker}'\
                AND( name LIKE '%{word}%' OR goods_code LIKE '%{word}%'OR desc LIKE '%{word}%'\
                OR price LIKE '%{word}%' OR goods_class LIKE '%{word}%'OR maker LIKE '%{word}%')")
    rows_list = cur.fetchall()
# カテゴリー：すべて以外、メーカー：すべて以外、フリーワード：空欄の場合
elif cate !='すべて' and maker !='すべて' and word =='':
    cur.execute(f"SELECT name,goods_code,price FROM goods WHERE goods_class='{cate}' AND maker='{maker}'")
    rows_list= cur.fetchall()
# トップページの表示
print(f'''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=0, maximum-scale=0, user-scalable=yes,shrink-to-fit=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0" name="viewport">
<meta content="yes" name="apple-mobile-web-app-capable">
<meta content="yes" name="apple-touch-fullscreen">
<meta content="black" name="apple-mobile-web-app-status-bar-style">
<meta content="320" name="MobileOptimized">

<title>商品一覧</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>

<link rel="stylesheet" type="text/css" href="/static/css/reset.css">
<link rel="stylesheet" type="text/css" href="/static/css/main.css">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.2/css/bootstrap.min.css">

<script src="https://cdn.staticfile.org/twitter-bootstrap/5.1.1/js/bootstrap.bundle.min.js"></script>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
      
<body>
 <div class="header_con bg-light bg-body">
   <div class="header" >
      <div class="welcome fl">三和電機へようこそ!</div>
      <div class="fr">
         <div class="login_btn fl">
               <a class="ud_line">ようこそ：{ user } 様</a>
               <form action="login.py" method="post">
                  <input type="hidden" name="is_active" value="1">
                  <input type="hidden" name="user" value="{ user }">
                  <input type="hidden" name="in_or_out" value="out">
                  <a class="ud_line" href="login.py"><input type="submit"  value="ログアウト" class="login_btn_top"></a>
               </form>
         </div>
      </div>
   </div>
</div>
<div class="search_bar clearfix">
    <img class="logo fl" alt="logo" src="/static/images/logo3.jpg" style="cursor: pointer;">

    <div class="guest_cart fr cart_anime">
        <div style="position: absolute">
            <form action="cart.py" method="post">
                <input type="hidden" name="user" value="{ user }">
                <a class="cart_name fl rounded"><input type="submit" class="cart_btn" value="カート"></a>
            </form>       
        </div>
    </div>
</div>
<nav id="naiver"  class="navbar1 navbar-expand-lg navbar_shadow mb-3 bg-body rounded">
    <div class="navbar-collapse" id="navbarNav">
        <div>
            <ul class="navbar-nav">
                <li style="font-weight: bold">
                <form action="top.py" method="post">
                    <input type="hidden" name="user" value="{ user }">
                    <input type="hidden" name="is_active" value="1">
                    <a class="nav_logo">
                    <img class="log_i" alt="top page" src="/static/images/home.png" > 
                    <input type="submit"  value="トップページ" class="nav_logo_sub">         
                    </a>   
                </form>
                </li>
            </ul>
        </div>
    </div>
</nav>
''')

# 検索結果
print(f'''
<div class="pagetitle">商品一覧</div>
<div class="main_wrap clearfix">
    <div class="r_wrap fr clearfix">
''')

# 検索結果
# 該当する商品情報がない場合、以下を表示する
if len(rows_list)==0:
    print('''
            <p><br>該当する商品はありません</p>
            
    ''')

# 検索結果
# 該当商品がある場合は、以下処理を行う
else:
    print('''
    <ul class="goods_type_list clearfix">
    ''')
    # 対象商品すべての商品の名前、画像などを並べて表示する    
    for name,goods_code,price in rows_list:
        print(f''' 
        <li class="shop_list">
            <div class="phn_con">
                <div>
                    <a><img alt="goods photo" class="rounded" src="/static/images/goodsの画像/(goods_code).jpg" alt="商品画像"></a>
                </div>
                <h4>
                    <a>{name}</a>                     
                </h4>
                <div class="operate">
                    <span class="prize"> ¥{price}</span>
                </div>
                <form action="goods.detail.py" method='post'>
                    <input type ='hidden' name ='shohin' value='{goods_code}'>
                    <input type ='hidden' name ='user' value='{user}'>
                    <input type ='submit' class=shohin_detail value='商品詳細'>
                </form >
            </div>
        </li>
        ''')

# 一覧の終了タグ
# <div class="footer">以降はフッター
print('''
            </ul>                    
    </div>
</div>
<div class="footer">
    <div class="foot_link">
        <a href="#">三和電機について</a>
        <span>|</span>
        <a href="#">お問い合わせ</a>
        <span>|</span>
        <a href="#">採用情報</a>
        <span>|</span>
        <a href="#">ヘルプ</a>
    </div>
</div>
</body>
</html>
''')
# DBを閉じる
cur.close()



