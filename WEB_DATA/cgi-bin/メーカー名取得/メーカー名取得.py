import codecs
import sys
import sqlite3

# windowsにおける文字化け回避
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

#DBと接続
con = sqlite3.connect('keden_web_cgi.db')
cur = con.cursor()

#goodsテーブルにあるメーカー名を重複なしで取得
cur.execute("SELECT DISTINCT maker FROM goods")
rows_maker = cur.fetchall()

#DBを閉じる
con.close()

# HTML
print("""
<!DOCTYPE html>
<html>
<body>
""")

for maker in rows_maker:
    print(f"""
    {maker[0]}<br>
    """
    )
print("""
</body>
</html>
""")

