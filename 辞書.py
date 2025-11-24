#変数animalsに辞書を定義
animals ={1:'dog',2:'cat',3:'bird'}
print(animals)
#空の辞書を定義
kara = {}
print(kara)

#dict関数を使用し、キーワード引数から辞書を作成
animal = dict(c = 'cat',d = 'dog')
print(animal)

#タプルのリストをdict関数に渡す
prefecture2 =dict([(2,'青森県'),(15,'新潟県'),(24,'三重県'),(37,'香川県')])
print(prefecture2)

#ke1を2つ含む辞書を定義
dict1 = {'key1':'りんご','key2':'みかん','key3':'ぶどう','key1':'いちご'}
print(dict1)

dict2 = {'key1':'晴れ','key2':'雨','key3':'くもり'}
#dict2にkey1が存在することを確認
print('key1' in dict2)
#dict2にkey2が存在しないことを確認
print('key2' not in dict2)

dict2 = {'key1':'晴れ','key2':'雨','key3':'くもり'}
#key2のvalueを取得
print(dict2['key2'])
#存在しないkey4の情報を取得
#print(dict2['key4'])
#key3のvalueを取得
print(dict2['key3'])
#デフォルト値に「指定されたkeyは存在しません」を設定
print(dict2.get('key4','指定されたkeyは存在しません'))
#デフォルト値を設定しない
print(dict2.get('key5'))

#新しい辞書animalsを定義
animals = {'サル':'monkey','ウサギ':'rabbit','ゾウ':'elephant','トラ':'tiger'}
#keyの一覧を取得
print(animals.keys())
#listとしてkeyの一覧を取得
print(list(animals.keys()))
#valueの一覧を取得
print(animals.values())
#keyを指定してvalueを取得
print(animals['サル'])
#辞書の中身をすべて取得
print(animals.items())

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}

#要素を追加
fruits['melon']=500
#値を上書き
fruits['peach']=300
print(fruits)

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}
#辞書に追加したい要素
fruits2 = {'melon':800,'cherry':400}
#要素を追加
fruits.update(fruits2)
print(fruits)

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}
#keyとvalueを追加
fruits.setdefault('banana',350)
print(fruits)

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}
#keyだけを追加
fruits.setdefault('mango')
print(fruits)

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}
fruits.setdefault('peach',100)
print(fruits)

d = {'国語':80,'算数':90,'理科':75,'社会':85}
#sum関数で4教科の合計点を求める
sougou = sum(d.values())
print(sougou)

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}
#要素を削除
del fruits['apple']
print(fruits)

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}
#複数の要素を削除
del fruits['apple'],fruits['peach']
print(fruits)

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}
#要素を削除
fruits.pop('lemon')
print(fruits)

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}
#デフォルト値を設定
#print(fruits.pop('kiwi','指定されたkeyは存在しません'))
#デフォルト値なし
#print(fruits.pop('kiwi'))

#辞書fruitsを定義
fruits = {'apple':100,'peach':250,'lemon':150}
#辞書内のすべての要素を削除
fruits.clear()
print(fruits)