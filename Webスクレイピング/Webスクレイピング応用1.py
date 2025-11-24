# モジュールのインポート
import requests
from bs4 import BeautifulSoup

# ヘッダー情報を設定
headers = {'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

# ウェブページを取得
get_html = requests.get('https://www.meti.go.jp/topic/data/e90622aj.html', headers=headers)
html = get_html.content

# BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(html, 'html.parser')

# .pdfで終わるリンクを見つける
pdf_link = soup.find('a', href=lambda href: href and href.endswith('.pdf'))

# リンクの存在チェック
if pdf_link:
    pdf_url = pdf_link.get('href')
    print(pdf_url)
else:
    print('PDFリンクが見つかりませんでした。')
