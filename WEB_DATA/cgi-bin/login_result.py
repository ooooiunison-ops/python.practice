import sys
import sqlite3
import urllib.parse
import os
import codecs

# 文字化け回避のため、標準出力をUTF-8に設定
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# HTMLからuserとpasswordを取得
text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form =urllib.parse.parse_qs(text)
user=form['user'][0]
password=form['password'][0]

# DBに接続
con = sqlite3.connect('kaden_web_cgi.db')
cur = con.cursor()

# ユーザー情報がDBに登録されているかをチェック
cur.execute(f"SELECT * FROM user_member_list WHERE user_id=? AND password=?",(user,password))

# 指定された資格情報を持つユーザーが存在するかどうかをチェック
result = 'ok' if list(cur) else 'ng'

# ユーザーが存在していた場合、is_activeが0(未ログイン)であるかチェック
if result == 'ok':
    # is_activeの値を取得
    cur.execute(f"SELECT * FROM user_member_list WHERE user_id=? AND password=?",(user,password))
    get_isactive= cur.fetchall()
    # is_activeが1ではない場合、1に更新する
    if get_isactive[0] != '1':
        cur.execute("UPDATE user_member_list \
        SET last_login = DATETIME(CURRENT_TIMESTAMP, '+9 hours'), is_active="1"\
        WHERE user_id = ?", (user,))
        
# DBの更新処理を確定
con.commit()

# DBを閉じる
con.close()

# ユーザーが存在していた場合、以下処理を行う
if result =='ok':
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

    <title>ログイン完了</title>
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
        <h1>ログインが完了しました</h1>
    </div>
    <div  class="move_btn">
        <form action='top.py' method='post'>
            <input type ='hidden' name='is_active' value='1'>
            <input type ='hidden' name='user' value='{ user }'>
            <img class="log_i" alt="top page" src="/static/images/home.png" > 
            <input type ='submit' value='トップページ' class='move_sub'>         
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
# ユーザーが存在していない場合、以下処理を行う
else:
    # ログインエラー
    # ログインへ画面へ戻る
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
        <h1>再度ログインしてください。</h1>
    </div>
    <div  class="move_btn">
        <form action='login.py' method='post'>
            <input type ='hidden' name='in_or_out' value='in'>
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