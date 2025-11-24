#モジュールをインポート
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

#指定URLのHTMLデータを取得
ur1 = 'https://www.data.jma.go.jp/stats/etrn/upper/view/hourly_usp.php?year=2015&month=4&day=20&hour=21&atm=&point=47582&view='
html = requests.get(ur1)

#BeautifulSoupでHTMLを解析
soup = BeautifulSoup(html.content,"html.parser")

#id = 'tablefix1'の<table>を抽出
table1 = soup.find("table",id='tablefix1')

#table1内の全thを抽出
th_all = table1.find_all('th')

#列タイトルをリストに格納
table1_column = []
for th in th_all:
    table1_column.append(th.string)

#table1内の全trを抽出
tr_all = table1.find_all('tr')

#先頭のtrは抽出済みなので飛ばす
tr_all = tr_all[1:]

#行と列の個数を算出し、ndarrayを作成
number_of_cols=len(table1_column)
number_of_rows=len(tr_all)
table1_data=np.zeros((number_of_rows,number_of_cols))

#各行のデータをndarrayに格納
for r,tr in enumerate(tr_all):
    td_all = tr.find_all('td')
    table1_data[r,:] = [td.string for td in td_all]

#データフレームを作成
df=pd.DataFrame(data=table1_data,columns=table1_column)

#CSVファイルに出力
df.to_csv('table1.csv',encoding="Shift-JIS")

#id = 'tablefix2'の<table>を抽出
table2 = soup.find('table',id ="tablefix2")

#table2内の全thを抽出
th_all2 = table2.find_all('th')

#列タイトルをリストに格納
table2_column = []
for th in th_all2:
    table2_column.append(th.get_text(strip=True))

#<table>内の全trを抽出
tr_all2 = table2.find_all('tr')

#先頭のtrは抽出済みなので飛ばす
tr_all2 = tr_all2[1:]

#行と列の個数を算出し、ndarrayを作成
number_of_col2 = len(table2_column)
number_of_rows2 = len(tr_all2)
table2_data = np.zeros((number_of_rows2,number_of_col2),dtype=np.float32)

#各行のデータをndarrayに格納
for r,tr in enumerate(tr_all2):
    td_all = tr.find_all('td')
    for c ,td in enumerate(td_all):
        try:
            table2_data[r,c]=td.string
        except ValueError:
            table2_data[r,c]=np.nan

#抽出したデータのDataFrameを生成
df2 = pd.DataFrame(data=table2_data,columns=table2_column)

#CSVファイルに出力
df2.to_csv("table2.csv",encoding='Shift-JIS')

#ターミナルに完了メッセージを表示
print('保存が完了しました')
