a = 10
def func():
    b = 20
    print(a)

print(a)
func()

def func():
    b = 20
    print(b)
func()

A = 10
def func():
    B = 20
    print(A)
#print(B)
func()

A = 'グローバル変数の値です'
def test1():
    B = 'test1のローカル変数の値です'
def test2():
    C = 'test2のローカル変数の値です'
print(A)
test1()
test2()

A = 'グローバル変数の値です'
def test1():
    B = 'ローカル変数の値です'
    print(A)
    print(B)
test1()

#グローバル変数
A = 'グローバル変数の値です'
def test1():
    #ローカル変数
    B = 'test1のローカル変数の変数Bです'
    #ローカル変数の表示確認
    print(B)
    #グローバル変数を呼び出す
    global A
    #グローバル変数の値を表示
    print(A)
    #グローバル変数の値を変更
    A = 'test1で値を変更しました'
    return A
#変更される前のグローバル変数の値を確認
print(A)
#ユーザー定義関数test1を呼び出し、グローバル変数の値が変更されたのを確認
print(test1())

strMon = '1月'

def Janmassage():
    global strMon
    strMon = '1月'
    print(strMon + 'は、31日まであります')

def Febmassage():
    global strMon
    strMon = '2月'
    print(strMon + 'は、29日まであります')

def Marmassage():
    global strMon
    strMon = '3月'
    print(strMon + 'は、31日まであります')

def Aprmassage():
    global strMon
    strMon = '4月'
    print(strMon + 'は、30日まであります')

def Maymassage():
    global strMon
    strMon = '5月'
    print(strMon + 'は、31日まであります')

def Junmassage():
    global strMon
    strMon = '6月'
    print(strMon + 'は、30日まであります')

def Julmassage():
    global strMon
    strMon = '7月'
    print(strMon + 'は、31日まであります')

def Augmassage():
    global strMon
    strMon = '8月'
    print(strMon + 'は、31日まであります')

def Sepmassage():
    global strMon
    strMon = '9月'
    print(strMon + 'は、30日まであります')

def Octmassage():
    global strMon
    strMon = '10月'
    print(strMon + 'は、31日まであります')

def Novmassage():
    global strMon
    strMon = '11月'
    print(strMon + 'は、30日まであります')

def Decmassage():
    global strMon
    strMon = '12月'
    print(strMon + 'は、31日まであります')

Janmassage()


a = 10
def func():
    b = 20
    print(a)
print(a)
func()

A = 'グローバル変数です'
def test1():
    global A
    A = '変更しました'
    print(A)
    return
test1()