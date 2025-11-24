import codecs
import sys
import os
import urllib.parse

# windowsにおける文字化け回避
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')


# フォームの取得
text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form = urllib.parse.parse_qs(text)

date = form['indate'][0]
number = form['innumber'][0]
name = form['inname'][0]
password = form['inpassword'][0]

# HTML
print(f"""
<!DOCTYPE html>
<html>
<body>
    生年月日{date}<br>
    好きな数字{number}<br>
    名前{name}<br>
    パスワード{password}<br>
</body>
</html>
"""
)

