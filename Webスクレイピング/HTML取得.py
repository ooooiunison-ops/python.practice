#モジュールをインポート
import requests
from bs4 import BeautifulSoup
import pandas as pd

#URLからHTMLを取得
ur1 = "https://www.fsa.go.jp/policy/nisa2/know/"
response = requests.get(ur1)

#BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(response.content, 'html.parser')

#HTML要素を取得
data_list = []
for details in soup.find_all('details',class_="js_details point_details"):
    if ques := details.find('span', class_="point_question_txt").get_text().strip():
        if ans := details.find('p',class_="point_answer_txt").get_text().strip():
            data_list.append([ques,ans.replace(' ','')])

#pandasのDataFrameを作成
df = pd.DataFrame(data_list)

#DataFrameをcsvファイルに書き込む
df.to_csv('NISAとは.csv',index=False,header=None,encoding='Shift-JIS')

#pandasを利用してcsvを表示
HTML_pd=pd.read_csv('NISAとは.csv',encoding='Shift-JIS')
print(HTML_pd)

