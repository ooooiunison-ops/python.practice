#モジュールのインポート
import requests
from bs4 import BeautifulSoup

#ヘッダー情報を設定
headers = {'User-Agent':
           "Mozilla/5.0(Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko)chrome/119.0.0.0 Safari/537.36"}

#ウェブページを取得
get_html = requests.get('https://www.meti.go.jp/topic/data/e90622aj.html', headers=headers)
html = get_html.content

#BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(html,'html.parser')

#aタグのすべての要素を取得
links = soup.findAll('a')

#リンクがPDFファイルであれば出力
for link in links :
    href = link.get('href')
    if href.endswith('.pdf'):
        print(href)
