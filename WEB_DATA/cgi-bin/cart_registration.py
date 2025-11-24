import sys
import sqlite3
import urllib.parse
import os
import codecs

# 文字化け回避のため、標準出力をUTF-8に設定
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# HTMLからユーザIDと商品コードと数量と単価を取得
text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form =urllib.parse.parse_qs(text)
user=form['user'][0]
shohin=form['shohin'][0]
tanka=form['tanka'][0]
suryo=form['suryo'][0]

# DBに接続
con = sqlite3.connect('kaden_web_cgi.db')
cur = con.cursor()


# DBからユーザーの会員情報を取得
cur.execute(f"SELECT user_name,addr_id,addr,tel,order_no FROM user_member_list WHERE user_id='{ user }'")
# 取得したデータを変数に格納
for x in cur:
     user_name=x[0]
     user_addr_id=x[1]
     user_addr=x[2]
     user_tel=x[3]
     user_order_no=x[4]


# DBにユーザーの購入中のオーダーがあるかを確認
cur.execute(f"SELECT * FROM df_order_info WHERE user_id='{ user }'AND is_paid='0'")
result='ok' if list(cur) else 'ng'

if result =='ok':
    # DBにユーザーの購入中のオーダーがある場合は商品のみ追加
    # DBからユーザーの購入中の注文IDを取得
    cur.execute(f"SELECT order_id FROM df_order_info WHERE user_id='{ user }'AND is_paid='0'")
    for x in cur :
        order_id = x[0]
    # DBにユーザーの購入中の注文IDと、カートに入れる商品コードと一致するレコードがあるかを確認
    cur.execute(f"SELECT * FROM df_order_goods WHERE oreder_id='{ order_id }'AND goods_code='{shohin}'")
    result2 = 'ok' if list(cur) else 'ng'
    if result2 =='ng':
        # DBにユーザーの購入中の注文IDで商品を追加
        cur.execute(f"INSERT INTO df_order_goods\
                     VALUES('{order_id}','{shohin}',{int(suryo)},{int(tanka)})")
    else:
        # DBにユーザーの購入中の商品の数量を加算
        cur.execute(f"UPDATE df_order_goods SET count=count +{int(suryo)} WHERE order_id='{ order_id }'AND goods_code='{shohin}'")
else:
    # DBにユーザーの購入中のオーダーが無い場合はオーダーと商品を追加
    # オーダー情報テーブル
    cur.execute(f"INSERT INTO df_order_info\
                (order_id,user_id,deli_addr_id,deli_addr,deli_tel)\
                VALUES('{user_name}{str(user_order_no)},'{user}','{user_addr_id}','{user_addr}','{user_tel}')")
    # オーダー商品テーブル
    cur.execute(f"INSERT INTO df_order_goods\
                VALUES('{user_name}{str(user_order_no)},'{shohin}',{int(suryo)},{int(tanka)})")

# DBの更新処理を確定      
con.commit()

# DBを閉じる
con.close()

# カート画面へ遷移
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

<title>カート登録完了</title>
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
                <a class="ud_line"> ようこそ: { user } 様</a>
                <form action='login.py' method='post'>
                    <<input type ='hidden' name='is_active' value='1'>>
                    <<input type ='hidden' name='user' value='{ user }'>>
                    <<input type ='hidden' name='in_or_oout' value='out'>>
                    <a class="ud_line"><input type='submit'value='ログアウト' class="login_btn_top"></a>
                </form> 
            </div>
        </div>
    </div>
</div>
<div class="search_bar clearfix">
    <img class="logo fl" alt="logo" src="/static/images/logo3.jpg" style="cursor: pointer;">
    <div class="guest_cart fr cart_anime">
        <div style="position: absolute">
        <form action='cart.py' method='post'>
        <input type='hidden' name='user' class='{ user }'>
        <a class="cart_name fl rounded"><input type='submit' value='カート' class='cart_btn'></a>
        </form>
        </div>
    </div>
</div>
    
<nav id="naiver"  class="navbar1 navbar-expand-lg navbar_shadow mb-3 bg-body rounded">
    <div class="navbar-collapse" id="navbarNav">
        <div>
            <ul class="navbar-nav">
                <li style="font-weight: bold">
                <form action ="top.py" method="post">
                    <input type ='hidden' name='user' value='{ user }'>
                    <input type ='hidden' name='is_active' value='1'>
                    <a class="nav_logo">
                    <img class="log_i" alt="top page" src="/static/images/home.png"> 
                    <input type ='submit' value='トップページ' class='nav_logo_sub'>         
                    </a> 
                </form>
                </li>
            </ul>
        </div>
    </div>
</nav>

<div class="reg_success search_bar clearfix">
    <h1>カートに登録されました。</h1>
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