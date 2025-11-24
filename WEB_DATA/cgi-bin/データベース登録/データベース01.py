import codecs
import sys
import os
import urllib.parse
import sqlite3

# windowsにおける文字化け回避
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')


# フォームの取得
text = sys.stdin.read(int(os.environ['CONTENT_LENGTH']))
form = urllib.parse.parse_qs(text)
id = form['inid'][0]
password = form['inpassword'][0]
blood = form['blood'][0]

#DBと接続
con = sqlite3.connect('blood.db')
cur = con.cursor()

#テーブルの作成(存在しない場合のみ作成)
cur.execute('''CREATE TABLE IF NOT EXISTS user_blood(
    id TEXT PRIMARY KEY
    password TEXT
    blood TEXT
)''')

# DBにユーザー新規登録
cur.execute(f"INSERT INTO user_blood\
            (id, password, blood) \
            VALUES('{id}','{password}','{blood}')")

# DBを更新
con.commit()

# DBを閉じる
con.close()

# HTML
print(f"""
<!DOCTYPE html>
<html>
<body>
    ID:{id}<br>
    パスワード:{password}<br>
    血液型:{blood}<br>
</body>
</html>
"""
)

