import sys
import sqlite3
import urllib.parse
import os
import codecs

# 文字化け回避のため、標準出力をUTF-8に設定
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# リクエストボディを受け取っているかの確認
content_length=os.environ.get('CONTENT LENGTH')
if content_length is None or content_length =='' or int(content_length) ==0:
    content_length='0'

# リクエストボディを受け取っている場合、以下の処理を行う 
if content_length!='0':
    text=sys.stdin.read(int(content_length))
    form=urllib.parse.parse_qs(text)

    # ログアウトボタンのフォームから来ていたら
    if form['in_or_out'][0]=='out':
        user=form['user'][0]

        con = sqlite3.connect('kaden_web_cgi.db')
        cur = con.cursor()
            
        # is_activeを'0'に変更し、ログイン解除する
        cur.execute("UPDATE user_member_list SET is_active='0' WHERE user_id=?",(user,))
        con.commit()
        con.close()

# ログインしたい場合はDB変更の処理は不要    
# ログイン画面HTML
print('''
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
    
    <title>ログイン</title>
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
<div class="login_top clearfix">
    <img class="logo fl" alt="logo" src="/static/images/logo3.jpg">
</div>
<div class="login_form_bg">
    <div class="login_form_wrap clearfix">
        <div class="login_banner fl"></div>
        <div class="login_form fr rounded">
            <div class="login_title clearfix">
                <h1>ログイン</h1>
                <form action='new_registration.py' method='post'>
                    <a><input type='submit' value='新規登録' class='reg_bar'></a>
                </form>
            </div>
            <div class="form_input log">
                <form action='login_result.py' method='post'>
                    <div class="mb-3">
                    <input type='text' name='user' class='form-control' required placeholder='ユーザー名'>
                    </div>
                    <div class="mb-3">
                    <input type='password' name='password' class='form-control' required placeholder='パスワード'>
                    </div>
                    <div class="pwd_error"></div>
                    <input type='submit' value='ログイン' class='log_btn'>
                </form>
            </div>
        </div>
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

<script type="text/javascript" src="/static/js/jquery-1.12.4.min.js"></script>
<script type="text/javascript" src="/static/js/jquery-ui.min.js"></script>
<script type="text/javascript" src="/static/js/slide.js"></script>
<script type="text/javascript">
    window.onresize = function () 
</script>
<script>
    Array.prototype.indexOf = function (val)   
</script>
      
</body>
</html>
''')