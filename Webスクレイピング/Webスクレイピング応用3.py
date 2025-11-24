#モジュールのインポート
import requests
from bs4 import BeautifulSoup

#ヘッダー情報を設定
headers = {'User-Agent':
           "Mozilla/5.0(Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko)chrome/119.0.0.0 Safari/537.36"}

#ウェブページを取得
get_html = requests.get('https://www.mhlw.go.jp/houdou_kouhou/index.html', headers=headers)
html = get_html.content

#BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(html,'html.parser')

#クラス属性がhtmlであるすべてのhtml要素をみつける
for element in soup.findAll(attrs = {'class':'m-txtM'}):
    #print(element)
    #各要素内で<a>要素を見つける
    names = element.findAll('a')
    #print(names)
    #<a>要素内のhref属性を取得
    for name in names :
        pdf_relative_path = name.get('href')
        print(pdf_relative_path)