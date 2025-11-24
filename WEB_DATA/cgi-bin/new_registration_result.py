import sys
import sqlite3
import urllib.parse
import os
import codecs

# 文字化け回避のため、標準出力をUTF-8に設定
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# HTMLからuser情報を取得
text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form =urllib.parse.parse_qs(text)
user=form['user'][0]
user_email=form['user_email'][0]
password=form['password'][0]
password_check=form['password_check'][0]
addr_id=form['addr_id'][0]
addr=form['addr'][0]
tel=form['tel'][0]

# パスワードと確認用パスワードが一致しない場合、以下処理を行う
if password != password_check:
    # 確認用パスワードエラー
    # ユーザー新規登録へ遷移
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

    <title>新規登録エラー</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>

    <link rel="stylesheet" type="text/css" href="/static/css/reset.css">
    <link rel="stylesheet" type="text/css" href="/static/css/main.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.2/css/bootstrap.min.css">

    <script src="https://cdn.staticfile.org/twitter-bootstrap/5.1.1/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <ssrc="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    </head>
          
    <body>
    <div class="header_con bg-light bg-body">
        <div class="header" >
            <div class="welcome fl">三和電機へようこそ!</div>
            <div class="fr">
                <div class="login_btn fl">
                    <form action='login.py' method='post'>
                        <input type ='hidden' name='in_or_out' value='in'>
                        <a class="ud_line" href="login.py"><input type ='submit' value='ログアウト' class="login_btn_top"></a>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <div class="search_bar clearfix">
        <img class="logo fl" alt="logo" src="/static/images/logo3.jpg"></a>
    </div>
    <div class="reg_success search_bar clearfix">
        <h1>確認用パスワードに誤りがあります。再度新規登録を行ってください。</h1>
    </div>
    <div  class="move_btn">
        <form action='new_registration.py' method='post'>
            <input type ='submit' value='新規登録' class="move_sub">        
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

# パスワードと確認用パスワードが一致した場合
else:
    result ='ok'
    try:
        # DBと接続
        con = sqlite3.connect('kaden_web_cgi.db')
        cur = con.cursor()
        
        # DBにユーザー新規登録（既にユーザーIDが登録されているかチェック。登録されていれば新たに追加することができないため）。'+9 hours'は日本時間(標準がイギリス時間のため)
        cur.execute("INSERT INTO user_member_list\
                    (user_id,password,last_login,user_name,user_email,user_joined,is_acctive,addr_id,addr,tel)\
                    VALUES(?,?,DATETIME(CURRENT_TIMESTAMP,'+9 hours'),?,?,DATETIME(CURRENT_TIMESTAMP,'+9 hours'),'1',?,?)",(user,password,user,user_email,addr_id,addr,tel))
    
    # 例外が発生した場合、resultを'ng'に設定
    except Exception as err:
        result='ng'

    # DBを更新
    con.commit()

    # DBを閉じる
    con.close()

    # 新規登録の処理が完了した場合、以下処理を行う
    if result =='ok':
        # 登録完了
        # トップページへ遷移
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

        <title>新規登録</title>
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
                    </div>
                </div>
            </div>
        </div>
        <div class="search_bar clearfix">
            <img class="logo fl" alt="logo" src="/static/images/logo3.jpg"></a>
        </div>
        <div class="reg_success search_bar clearfix">
            <h1>新規登録が完了しました。</h1>
        </div>
        <div  class="move_btn">
            <form action='top.py' method='post'>
                <input type ='hidden' name='is_active' value='1'>
                <input type ='hidden' name='user' value='{ user }'>
                <img class="log_i" alt="top page" src="/static/images/home.png" > 
                <input type='submit' value='トップページ' class='move_sub'>         
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

    # 既に登録されている場合、以下処理を行う
    elif result =='ng':
        # 新規登録画面へ戻る
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

        <title>新規登録エラー</title>
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
                        <form action='login.py' method='post'>
                            <input type ='hidden' name='in_or_out' value='in'>
                            <a class="ud_line" href="login.py"><input type ='submit' value='ログイン' class='login_btn_top'></a>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <div class="search_bar clearfix">
            <img class="logo fl" alt="logo" src="/static/images/logo3.jpg">
        </div>
        <div class="reg_success search_bar clearfix">
            <h1>既に登録されているアカウントです。再度、新規登録を行ってください。</h1>
        </div>
        <div  class="move_btn">
            <form action='new_registration.py' method='post'>
            　　　<input type ='submit' value='新規登録' class="move_sub">        
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