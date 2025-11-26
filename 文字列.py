a = 'Good Morning Python'
bunkatu = a.split()
print(bunkatu)

moji = 'にんじん/玉ねぎ/じゃがいも'
b = moji.split('/')
print(b)

a = 'apple prange'
#'e'を先頭から検索
print(a.find('e'))
#'e'を末尾から検索
print(a.rfind('e'))

b = 'apple grape'
#'a'を先頭から検索
print(b.index('a'))
#'a'を末尾から検索
print(b.rindex('a'))

c = 'dog cat bird'
#'z'を先頭から検索
#print(c.find('z'))
#'z'を末尾から検索
#print(c.index('z'))

a = 'こんにちは！パイソン！'
print(a.replace('こんにちは','こんばんは'))
print(a.replace('パイソン！','Python'))

a = 'hello,python'
b = 'GOOD MOONING'
print(a.upper())
print(b.lower())

kakunin = 'abcdefg'
#前方一致しているか確認
print(kakunin.startswith('abc'))
#後方一致しているか確認
print(kakunin.endswith('dfg'))

cut = 'Hello!Hello!Python'
print(cut.count('H'))
print(cut.count('h'))

#変数に代入
name = '花子'
#format()メソッドで変数を呼び出し
print('私の名前は{}です。'.format(name))


#変数に代入
name = '花子'
age = 25
hometown = '東京'
#format()メソッドで変数を呼び出し
print('私の名前は{}です。年齢は{}で、{}出身です。'.format(name,age,hometown))

x = 30
y = 13
print('{0}-{1}={2}'.format(x,y,x-y))

x = 10
y = 25
print('{1}+{0}={2}'.format(x,y,x+y))

name1 = '田中'
name2 = '太郎'
age = 20
print('私の名前は{A}{B}です。{c}才です。'.format(A=name1,B=name2,c=age))


name='小春'
name2='鈴木花代'
age= 5
age2= 30

print(f'私の名前は{name}です。{age}才です。')
print(F'あの人の名前は{name2}です。{age2}才です')


x = 'I Study Python'
x.split()
print(x.upper())

x = 'I Study Python'
print(x.replace('Python','Ruby'))

x = 10
y = 25
z = 50
print(f'60は"{z}+{x}"や"{y}+{y}+{x}"などで求めることができます。')

a='野菜'
b='果物'
print('この八百屋の{A}と{B}はとてもおいしいです。'.format(A=a,B=b))