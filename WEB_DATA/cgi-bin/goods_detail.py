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
shohin=form['shohin'][0]
# DBに接続
con = sqlite3.connect('kaden_web_cgi.db')
cur = con.cursor()

#  データベースからデータを取得
cur.execute(f"SELECT name,goods_code,desc,price FROM goods WHERE goods_code='{shohin}'")
rows_detail = cur.fetchall()
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

<title>商品詳細</title>
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
                <a class="ud_line">!--ようこそ: { user } 様--</a>
                <form action='login.py' method='post'>
                    <input type ='hidden' name='is_active' value='1'>
                    <input type ='hidden' name='user' value='{ user }'>
                    <input type ='hidden' name='in_or_out' value='out'>
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
            <form action ='cart.py' method="post">
                <input type ='hidden' name='user' value='{ user }'>
                <a href="cart.py" class="cart_name fl rounded"><input type="submit" class="cart_btn" value="カート"></a>
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
                    <a class="nav_logo" href= "top.py">
                    <img class="log_i" alt="top page" src="/static/images/home.png" > 
                        <input type ='submit' value='トップページ' class='nav_logo_sub'>         
                    </a>     
                </form>
                </li>
            </ul>
        </div>
    </div>
</nav>
''')

# 商品詳細
print('''
<div class="pagetitle">商品詳細</div>
''')

# 商品詳細
# 商品の名前、画像、金額などの詳細を表示
for name,goods_code,desc,price in rows_detail:
    print(f'''
        <form action='cart_registration.py' method='post'>
            <input type ='hidden' name='user' value='{ user }'>
            <input type ='hidden' name='shohin' value='{ goods_code }'>
            <input type ='hidden' name='tanka' value='{ price }'>
            <div>
                <div class="goods_detail_con clearfix rounded">
                    <div class="carousel slide" ">
                        <img src="/static/images/goodsの画像/{ goods_code}.jpg" alt="{ name }">            
                    </div>

                    <div class="goods_detail_list fr">
                        <h3>{ name }</h3>
                        <p></p>
                        <div class="prize_bar rounded">
                            <span class="show_pirze">¥<em>{ price }</em></span>
                        </div>
                        <div class="goods_num clearfix">
                            <div class="num_name fl">数 量：</div>
                            <div class="num_add fl" style="box-sizing:content-box">
                                <input type ='text' name='suryo' class="num_show fl" value='1' id='good_count'>
                                <a class="add fr decoration" onclick="addGoodCount()">+</a>
                                <a class="minus fr decoration" onclick="subGoodCount()">-</a>
                            </div>
                        </div>
                        <div class="operate_btn">
                            <input type ='submit' value='カートに入れる' class='add_cart_btn'>
                        </div>
                    </div>
                </div>
            </div>
        </form>
        <div class="container">
            <!-- Tab 欄 -->
            <ul class="nav nav-tabs" id="productTab" role="tablist">
                <li class="nav-item">
                    <a class="nav-link active" id="product-detail-tab" data-toggle="tab" href="#productDetail" role="tab" aria-controls="productDetail" aria-selected="true">商品情報</a>
                </li>
            </ul>
            <!-- Tab 内容 -->
            <div class="tab-content" id="myTabContent">
                <!-- 商品詳細 -->
                <div class="tab-pane fade show active" id="productDetail" role="tabpanel" aria-labelledby="product-detail-tab">
                    <div class="main_wrap clearfix">
                        <div class="r_wrap fr clearfix">
                            {desc}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    ''')

# 商品詳細の終了タグ
# <div class="footer">以降フッターと数量カウント用のjavascript
print('''
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

<script type="text/javascript">
    var good_count = 1;  // 商品数
    function addGoodCount() {
        good_count += 1;
        $('#good_count').val(good_count)
    }
    function subGoodCount() {
        if (good_count === 1) return
        good_count -= 1;
        $('#good_count').val(good_count)
    }
</script>

</body>
</html>
''')


