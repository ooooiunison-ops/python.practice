import sys
import codecs

# 文字化け回避のため、標準出力をUTF-8に設定
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# ユーザー新規登録画面
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
<div class="register_con">
  <div class="l_con fl">
      <img class="logo fl" alt="logo" src="/static/images/logo3.jpg">
      <div class="reg_slogan">三和電機へようこそ！</div>
      <div class="reg_banner"></div>
   </div>

   <div class="r_con fr">
      <div class="reg_title clearfix">
            <h1>新規登録</h1>
            <form action='login.py' method='post'>
               <input type ='hidden' name='in_or_out' value='in'>
               <a class="ud_line" href="login.py"><input type ='submit' value='ログアウト' class="login_btn_top"></a>
            </form>
      </div>
      <div class="reg_form clearfix">
            <form action='new_registration_result.py' method='post'>
               <ul>
                  <li>
                        <label>ユーザー名:</label>
                        <input type='text'
                               name='user'
                               id='user_name'
                               class='form_control'
                               required
                               minlength='2'
                               maxlength='20'
                               placeholder='最低2文字、最長20文字まで'
                               oninvalid='setCustomValidity("ユーザー名は2～20文字までにしてください");'
                               oninput="setCustomValidity('');">
                  </li>
                  <li>
                        <label>メールアドレス:</label>
                        <input type='email'
                               name='user_email'
                               id='email'
                               class='form_control'
                               required
                               maxlength='100'
                               oninvalid='setCustomValidity("メールアドレスを確認してください");'
                               oninput="setCustomValidity('');">
                  </li>
                  <li>
                        <label>パスワード:</label>
                        <input type='password'
                               name='password'
                               id='pwd'
                               class='form_control'
                               required
                               minlength='8'
                               maxlength='20'
                               placeholder='最低8文字、最長20文字まで'
                               oninvalid='setCustomValidity("パスワードは8～20文字までにしてください");'
                               oninput="setCustomValidity('');">
                  </li>
                  <li>
                        <label>パスワード(確認):</label>
                        <input type='password'
                               name='password_check'
                               id='cpwd'
                               class='form_control'
                               required
                               minlength='8'
                               maxlength='20'
                               placeholder='上記のパスワードと同じように'
                               oninvalid='setCustomValidity("もう一度パスワードを入力してください");'
                               oninput="setCustomValidity('');">
                  </li>
                  <li>
                        <label>郵便番号:</label>
                        <input type='password'
                               name='addr_id'
                               class='form_control'
                               required
                               pattern="[0-9]{{7}}"
                               placeholder='〒 ハイフン(-)不要'
                               oninvalid='setCustomValidity("郵便番号を入力してください");'
                               oninput="setCustomValidity('');">
                  </li>
                  <li>
                        <label>住所:</label>
                        <input type='text'
                               name='addr'
                               class='form_control'
                               required
                               maxlength='100'
                               oninvalid='setCustomValidity("住所を入力してください");'
                               oninput="setCustomValidity('');">  
                  </li>
                  <li>
                        <label>電話番号:</label>
                        <input type='text'
                               name='tel'
                               class='form_control'
                               required
                               pattern="[0-9]{{0,20}}"
                               placeholder='ハイフン(-)不要'
                               oninvalid='setCustomValidity("電話番号を入力してください");'
                               oninput="setCustomValidity('');">
                  </li>
                  <li>
                        <input type ='submit' value='新規登録' class="reg_btn">
                  </li>
               </ul>
            </form>
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
</body>
</html>
''')


