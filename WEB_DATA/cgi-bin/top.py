# ★ここから記述してください。
import codecs
import os
import sqlite3
import sys
import urllib.parse

# 文字化け回避のため、標準出力をUTF-8に設定
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# HTMLからユーザーを取得
text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form = urllib.parse.parse_qs(text)
user = form['user'][0]

# DBと接続
con = sqlite3.connect('kaden_web_cgi.db')
cur = con.cursor()

# データベースからデータを取得
# カテゴリー別ランキング1位の商品情報取得
cur.execute("SELECT goods_rank.*,goods.name,goods.price FROM goods_rank JOIN goods ON goods_rank.goods_code WHERE goods_rank.rank =1")
rows_rank =cur.fetchall()
# goodsテーブルにある種類を重複なしで取得
cur.execute("SELECT DISTINCT goods_class FROM goods")
rows_class = cur.fetchall()

# goodsテーブルにあるメーカー名を重複なしで取得
cur.execute("SELECT DISTINCT maker FROM goods")
rows_maker = cur.fetchall()

# DBを閉じる
con.close()

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

<title>トップページ</title>
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
               <a class="ud_line">ようこそ:{user}様</a>
               <form action ="login.py" method ="post">
                  <input type = "hidden" name = "is_active" value ="1">
                  <input type = "hidden" name = "user" value="{user}">
                  <input type = "hidden" name = "in_or_out" value ="out">
                  <a class="ud_line" href="login.py"><input type ="submit" value="ログアウト" class="login_btn_top"></a>
               </form>
         </div>      
      </div>
   </div>
</div>
<div class="search_bar clearfix">
    <img class="logo fl" alt="logo" src="/static/images/logo3.jpg">

    <div class="guest_cart fr cart_anime">
        <div style="position: absolute">
        <form action ="cart.py" method ="post">
            <input type = "hidden" name = "user" value ="{user}">
            <a class="cart_name fl rounded"><input="submit" class="cart_btn" value="カート"></a>
        </form>       
        </div>
    </div>
</div>

    
<nav id="naiver"  class="navbar1 navbar-expand-lg navbar_shadow mb-3 bg-body rounded">
    <div class="navbar-collapse" id="navbarNav">
        <div>
            <ul class="navbar-nav">
            <a class="nav_logo">
                <li style="font-weight:bold">
                    <img class="log_i" alt="top page" src="/static/images/home.png">
                    トップページ
                </li>
            </a>
            </ul>
        </div>
    </div>
</nav>
''')

# 人気商品欄表示
# 見出し
print(f'''
<div class="list_model">
    <div style="margin: 15px 0">
        <h4 clas="headline">人気商品</h4>
    </div>
    <div class="goods_con clearfix">
        <ul class="goods_list  rounded">
''')

# 人気商品欄表示
# 各部門の1位の商品を表示
for goods_code,rank,goods_class,name,price in rows_rank:
    print(f'''
    <li class="rounded">
        <h4>
    ''')
    # もしgoods_classに「・」が含まれていた場合、「・」の前と「・」の後で改行する
    if "." in goods_class:
        print(f'''
        <span>
            {goods_class.split(".")[0]}<br>
            {goods_class.split(".")[1]}
        </span>
        部門<br>
    ''')
    # 「・」がない場合、そのままgoods_classを表示する
    else:
        print(f'''
        <span>{goods_class}</span>部門
        ''')

    print(f'''
        <!--★ここにコードを記述してください。-->                  
        </h4>
        <img class="rounded" src="/static/images/goodsの画像/{goods_code}.jpg" alt="商品画像">
        <div class="prize">￥{price}
        </div>
        <form action ="goods_detail.py?get_goods_code={goods_code}"method="post">
            <input type ="hidden" name="user" value="{user}">
            <input type ="hidden" name="shohin" value="{goods_code}">
            <input type ="submit" class="shohin" detail value="商品詳細">
        </form>
     </li>
    ''') #ループ終了
    
# 人気商品欄表示
# 終了タグ    
print(f'''
        </ul>
    </div>
</div>
''')

# 検索欄
print(f'''
<div class="list_model">
    <div style="margin: 15px 0">
        <h4 class="headline">商品検索</h4>
    </div>
<div class="goods_con clearfix">
    <div class="r_wrap fr clearfix">
        <form action="goods_list.py" method="post">
            <input type ="hidden" name="user" value="{user}">
            <div class="rounded sort_bar_f">
''')

# 検索欄
# カテゴリーのプルダウンデフォルトの中の「すべて」を表示
print(f'''
                <div class="sort_bar">
                    <a>カテゴリー:</a>
                        <select name="cate" class="select_box">
                            <option>すべて</option>
''')

# 検索欄
# カテゴリーの種類をプルダウンに表示
for goods_class in rows_class:
    print(f'''
    <option value={goods_class[0]}>{goods_class[0]}<option>
    ''') #ループ終了

# 検索欄
# 終了タグ
print(f'''
                        </select>                       
                </div>
''')

# 検索欄
# カテゴリーのプルダウンデフォルトの中の「すべて」を表示
print(f'''
                <div class="sort_bar">
                    <a>メーカー:</a>
                        <select name="maker" class="select_box">
                            <option>すべて</option>
''')

# 検索欄
# メーカーの種類をプルダウンに表示
for maker in rows_maker:
    print(f'''
    <option value={maker[0]}>{maker[0]}</option>      
    ''')

# 検索欄
# 終了タグ                                   
print(f'''
                        </select>                           
                </div>
''')               

# 検索欄
# キーワード検索窓
# <div class="footer">以降はフッター                                   
print(f'''              
                <div class="sort_bar">
                    <a>フリーワード:</a>
                        <div class="search_con fl rounded">
                                <input type="text" name="word" class="input_text fl form_con"placeholder="フリーワード">
                        </div>
                </div> 

                <div class="sort_bar">
                    <a class=fr_word><input type="submit" class="input_btn" value="検索"></a>
                </div>
            </div>
        </form>
    </div>
</div>
<br>
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


