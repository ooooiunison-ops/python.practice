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
in1 = form['input01'][0]
in2 = form['input02'][0]

# calcメソッドの定義
calc = int(in1) + int(in2)
    

# HTML
print(f"""
<!DOCTYPE html>
<html>
<body>
    {in1} + {in2} = {calc}
</body>
</html>
"""
)

