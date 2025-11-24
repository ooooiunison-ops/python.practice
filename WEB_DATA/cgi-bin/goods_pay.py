import sys
import sqlite3
import urllib.parse
import os
import codecs

# 文字化け回避のため、標準出力をUTF-8に設定
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# HTMLから検索条件を取得
text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form =urllib.parse.parse_qs(text)
user = form['user'][0]
order_id = form['order_id'][0]

try :
    # DBに接続
    con = sqlite3.connect('kaden_web_cgi.db')
    cur = con.cursor()

    # DBトランザクション開始
    cur.execute('BEGIN TRANSACTION;')

    # DBを支払い完了に更新
    cur.execute(f" UPDATE  df_order_info SET is_paid='1' WHERE order_id='{order_id}'")

    # DBのユーザーマスタのオーダー発行番号を更新
    cur.execute(f" UPDATE  user_member_list SET order_no=order_no + 1 WHERE user_id='{user}'")

    # DBトランザクション確定
    con.commit()

    # DBを閉じる
    con.close()

    # 支払い完了画面の表示
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

    <title>支払い完了</title>
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
                <a class="ud_line">ようこそ: { user } 様</a>
                <form action='login.py' method='post'>
                    <input type ='hidden' name='is_active' value='1'>
                    <input type ='hidden' name='user' value='{ user }'>
                    <input type ='hidden' name='in_or_out' value='out'>
                    <a class="ud_line" href="login.py"><inpit type='submit' value='ログアウト' class='login_btn_top'></a>
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
                <fotm action='top.py' method='post'>
                        <input type ='hidden' name='is_active' value='1'>
                        <input type ='hidden' name='user' value='{ user }'>
                        <a class="nav_logo" href= "top.py">
                        <img class="log_i" alt="top page" src="/static/images/home.png" > 
                        <input type='submit' value='トップページ' class='nav_logo_sub'>       
                        </a>
                </form>
                </li>
                </ul>
            </div>
    </div>
    </nav>

    <div class="pay">
    <h2><br>ご注文ありがとうございました。<br>以下の注文の支払いが完了しました。</h2>
    <p>注文ID:{ order_id }<br></p>
    <br>
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

# 例外が発生した場合、以下の処理を行う
except Exception as e:
   # DB接続が完了している場合
    if con :
        # ロールバックを実行し、現在のトランザクションで行われたすべての変更を取り消す
        con.rollback()
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

            <title>ログインエラー</title>
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
                </div>
            </div>

            <div class="search_bar clearfix">
                <img class="logo fl" alt="logo" src="/static/images/logo3.jpg"></a>
            </div>
            <div class="reg_success search_bar clearfix">
                <h1>注文処理中にエラーが発生しました。<br>大変恐れ入りますが、再度ログインからお手続きをお願いいたします。</h1>
            </div>
            <div  class="move_btn">
                <form action='login.py' method='post'>
                    <input type ='hidden' name='user' value='{ user }'>
                    <input type ='hidden' name='is_active' value='1'>
                    <input type ='hidden' name='in_or_out' value='out'>
                    <input type ='submit' value='ログイン画面へ戻る' class='move_sub'>
                </form>
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

# どの処理を実行した後でも、最後に以下処理を実行する
finally:
    # もしDBが接続されていれば、DBを閉じる
    if con:
        con.close()




