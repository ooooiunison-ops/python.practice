#モジュールをインポート
import PyPDF2
import requests
from bs4 import BeautifulSoup
import pandas as pd

#URLからHTMLを取得
ur1 = "https://www.mhlw.go.jp/houdou_kouhou/index.html"
get_html = requests.get(ur1)

#BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(get_html.content,'html.parser')

#PDFのURLを取得
for element in soup.find_all(attrs={'class':"m-txtM"}):
    names = element.find_all('a')
    for name in names:
        pdf_relative_path = name.get('href')

#PDFファイルをダウンロードして保存
response = requests.get(pdf_relative_path)
with open ('基礎指針の趣旨.pdf',"wb")as pdf_file:
    pdf_file.write(response.content)

#ダウンロードしたPDFファイルを読み込む
with open('基礎指針の趣旨.pdf',"rb")as file:
    reader = PyPDF2.PdfReader(file)

#基本指針の趣旨を格納するリストを作成
    summmaries = []

#PDFファイルから各ページのテキストを抽出
    for page_num in range (len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()

#テキストの中から基本指針の趣旨を探す
        if "基本指針の趣旨" in text:
            start_index = text.find("基本指針の趣旨")

#"基本指針の趣旨"が含まれる部分以降のテキストを抽出
            relevant_text= text[start_index:]
            summmaries.append(relevant_text)

#DataFrameにデータを格納
df = pd.DataFrame(summmaries)

#csvファイルとして保存
df.to_csv('厚生労働省広報基礎指針.csv',
          index = False,header=None,encoding='Shift-JIS')
#csvファイルに保存しましたを表示
print('csvファイルに保存しました')
