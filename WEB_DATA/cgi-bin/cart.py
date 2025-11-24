import sys
import sqlite3
import urllib.parse
import os
import codecs

# 文字化け回避のため、標準出力をUTF-8に設定
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# HTMLから情報を取得
text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form =urllib.parse.parse_qs(text)
user=form['user'][0]
order_id = form.get('order_id',[''])[0]
goods_code = form.get('goods_code',[''])[0]

# DBに接続
con = sqlite3.connect('kaden_web_cgi.db')
cur = con.cursor()

# 商品削除処理
if goods_code:
    # カートページで削除ボタンが押された場合
    # オーダー商品テーブルから対象レコートを削除
    cur.execute(f" DELETE FROM df_order_goods WHERE order_id='{order_id}' AND goods_code='{goods_code}'")
    # オーダー商品テーブルから対象オーダー番号のレコードを取得
    cur.execute(f" SELECT * FROM df_order_goods WHERE order_id='{order_id}'")
    result2 = "ok" if list(cur) else "ng"
    # オーダー商品テーブルに対象オーダー番号のレコードがない場合
    if result2 == "ng":
        # オーダー情報テーブルから、対象オーダー番号のレコードを削除
        cur.execute(f" DELETE FROM df_order_info WHERE order_id='{order_id}' AND is_paid='0'")
        order_id =""
        
    # DBの更新処理を確定
    con.commit()

# DBより指定ユーザの未支払いカート存在確認
cur.execute(f" SELECT * FROM df_order_info WHERE user_id='{user}' AND is_paid='0'")
result = 'ok' if list(cur) else 'ng'

# DBより指定ユーザの未支払いオーダー番号取得
if result =='ok':
    cur.execute(f" SELECT order_id FROM df_order_info WHERE user_id='{user}' AND is_paid='0'")
    for x in cur:
        order_id= x[0]

    # DBより未支払いオーダー情報を取得
    cur.execute(f" SELECT df_order_goods.goods_code,goods.name,df_order_goods.price,df_order_goods.count,df_order_goods.price * df_order_goods.count AS subtotal\
                FROM df_order_goods\
                JOIN goods ON df_order_goods.goods_code=goods.goods_code\
                WHERE order_id='{order_id}' ")
    cart_list = cur.fetchall()

    # DBより未支払いオーダー情報の合計金額、合計数量を取得
    cur.execute(f" SELECT SUM(price * count) AS total_amount,SUM(count)AS total_count\
                FROM df_order_goods\
                WHERE order_id='{order_id}'")
    cart_total = cur.fetchall()


# DBを閉じる
con.close()

# カート画面の表示
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

<title>カート</title>
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
               <form action = 'login.py' method='post'>
                  <input type ='hidden' name='is_active' value='1'>
                  <input type ='hidden' name='user' value='{ user }'>
                  <input type ='hidden' name='in_or_out' value='out'>
                  <a class="ud_line" href="login.py"><input type ='submit' value='ログアウト' class="login_btn_top"></a>
               </form>
         </div>
      </div>
   </div>
</div>
<div class="search_bar clearfix">
    <img class="logo fl" alt="logo" src="/static/images/logo3.jpg">
</div>
<nav id="naiver"  class="navbar1 navbar-expand-lg navbar_shadow mb-3 bg-body rounded">
    <div class="navbar-collapse" id="navbarNav">
        <div>
            <ul class="navbar-nav">
                <li style="font-weight: bold">
                <form action ='top.py' method='post'>
                    <input type ='hidden' name='user' value='{ user }'>
                    <input type ='hidden' name='is_active' value='1'>
                    <a class="nav_logo">
                    <img class="log_i" alt="top page" src="/static/images/home.png" > 
                    <input type ='submit' value='トップページ' class='nav_logo_sub'>          
                    </a>   
                </form>
                </li>
            </ul>
        </div>
    </div>
</nav>
<div class="mypg_title clearfix">
   <h1>カート</h1>
</div>
''')

#カートに商品がある場合、以下を表示する
if order_id !='':
    #カート登録商品一覧の項目名
    print(f'''
    <br>
    <ul class="cart_list_th clearfix rounded-top">
        <li class="col01">商品名</li>
        <li class="col03">商品価格</li>
        <li class="col04">数量</li>
        <li class="col05">小計</li>
    </ul>
    ''')
    #カート登録商品一覧
    for goods_code,name,price,count,subtotal in cart_list:
        print(f'''
        <ul class="cart_list_td clearfix">
            <li class="col02"><img class="rounded" src="/static/images/goodsの画像/{goods_code}.jpg" alt="商品画像" width="190" height="130"></li>
            <li class="col03">{ name }</li>
            <li class="col04">{ price }円</li>
            <li class="col05">{ count }</li>
            <li class="col06">{ subtotal }円</li>
            <li class="col08">
                <form action="cart.py" method="post">
                    <input type ='hidden' name='user' value='{ user }'>
                    <input type ='hidden' name='order_id' value='{ order_id }'>
                    <input type ='hidden' name='goods_code' value='{ goods_code }'>
                    <input type ='submit' value='削除' class="btn btn-outline-secondary">
                </form>
            </li>
        </ul>
        ''')
    for total_amount,total_count, in cart_total:
        print(f'''
        <ul class="settlements rounded-bottom">
            <li class="col03">合計(送料別途)：<span>¥</span><em id="all_price">{ total_amount }</em><br>計<b id="shop_count">{ total_count }</b>件商品</li>
        </ul>
        ''')
    #注文を確定ボタン
    print(f'''
    <br>
    <div class="log">
        <form action='goods_pay.py' method='post'>
            <input type ='hidden' name='user' value='{ user }'>
            <input type ='hidden' name='order_id' value='{ order_id }'>
            <input type ='submit' value='注文を確定' class="btn btn-primary" style="height: 65px; width: 163px;;margin-bottom: 10px;font-size: 22px">
        </form>
    </div>
    ''')

#カートが空の場合、以下を表示する
else:  
    print(f'''
    <div class="pay">
        <h2><br>現在カートに商品はありません。</h2>
        <br>
    </div>
    ''')

#フッター
print(f'''
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