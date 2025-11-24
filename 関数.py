#関数を定義
def say_hello():
    print('Hello,Python!')
#関数を呼び出し
say_hello()

#関数cookieを定義
def cookie(topping):
    print('クッキー生地を作成します')
    print('作成したクッキー生地に'+ topping +'を合わせて焼きます')
    print(topping+'のクッキーができました')
#関数を呼び出し
cookie('チョコ')

#関数を定義
def add(num1,num2):
    print(num1 + num2)
#関数を呼び出し 
add(10,20)

#関数を定義
def add(a,b):
    result= a + b
    return result
#関数を呼び出し 
print(add(5,7))

def add(x,y):
    if x + y ==10:
        return('xとyの合計は10です')
    return x + y

#xとyの合計が10となる引数を渡す
print(add(3,7))
#xとyの合計が10以外の引数を渡す
print(add(2,3))

def add(num1,num2):
    if num1 + num2 < 10:
        return num1 + num2
#num1とnum2の合計が10以上の引数を渡す 
print(add(7,8))

#関数を定義
def hello(greeting):
    print(greeting)
#関数helloを変数に代入
aisatsu = hello
#変数aisatsuを代入
aisatsu('Hello Python!')

def say_hello(a,b,c,):
    print('朝は',a,'、昼は',b,'、夜は',c,'といいます')

say_hello('おはよう','こんにちは','こんばんは')

def english(a,b,c,):
    print('一は',a,'、二は',b,'、三は',c,'と言います')

english(b ='two', c ='three', a ='one')

def func(a,b,c,d):
    print('a:',a)
    print('b:',b)
    print('c:',c)
    print('d:',d)
#位置引数とキーワード引数を使用
func(4,3,d=1,c=2)

#デフォルト引数のある関数addを定義
def add (a=20, b=15):
    print(a+b)

print('デフォルト値が優先:')
add()
print('実引数が優先:')
add(5,3)

#可変長位置引数を含む関数を定義
def alphabet(a2,b2,*args):
    print(a2)
    print(b2)
    print(args)

#関数を呼び出し
alphabet('a','b','c','d','e')

#可変長位置引数を含む関数を定義
def alphabet(a2,b2,*args):
    print(a2)
    print(b2)
    print(*args)
#関数を呼び出し
alphabet('p','y','t','h','o','n')

#可変長位置引数を含む関数を定義
def hello(*args):
    for i in args:
        print(i)
#関数を呼び出し
hello('h','e','l','l','o')

#可変長キーワード引数を使用した関数を定義
def keyword(**kwargs):
    print(kwargs)

#キーワード引数を使用して関数を呼び出し
keyword(a = 'apple',b = 'banana',c = 'cherry')

#関数を定義
def add(a,b,c,):
    return a+b+c
#リストを作成
list =[10,15,20]
#作成したリストを関数addへ渡す
print(add(*list))
#関数を定義
def moji(a,b,c,):
    return a+b+c
#タプルを作成
tuple = ('おはよう！','今日は','いい天気ですね')
#作成したタプルを関数mojiへ渡す
print(moji(*tuple))

#関数を定義
def func(a2,b2,c2):
    print(a2,'と',b2,'と',c2)
#辞書を定義
dic = {'a2':'犬','b2':'猫','c2':'ウサギ'}
#辞書を関数funcの因数へ渡す
func(**dic)

#関数を定義
def ex(a,b,c):
    return a,b,c
#リストを作成
list=['にんじん']
#タプルを作成
tuple=('玉ねぎ',)
#辞書を定義
dic = {'c':'じゃがいも'}

print(ex(*list,*tuple,**dic))

#関数を定義
def ex(a,b,c,d):
    return a,b,c,d
#リストを作成
list=['りんご']
#タプルを作成
tuple=('ぶどう',)
#辞書を定義
dic = {'c':'もも','d':'メロン'}

print(ex(*list,*tuple,**dic))

#関数を定義
def outer_func(a,b):
    #関数内関数を定義
    def inner_func(c,d):
        return c + d
    #inner_funcを呼び出し+変数に代入
    e = inner_func(a,b)
    #変数e(inner_func)の結果を表示
    print(e)

#outer_funcを呼び出し
outer_func(1,3)

#関数を定義
def outer_func(a):
    #関数内関数を定義
    def inner_func(b):
        return a + b
    #inner_funcの処理結果を返す
    return inner_func

#outer_funcに10を渡す＋変数に代入
c = outer_func(10)

#outer_funcを呼び出し
print(c(20))