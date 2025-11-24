print('abc')
print("おはよう")
print('仙崎恵磨')

print("今日は","雨です")
print('今日は','曇りです')

print('今日は'+'雨です')
print('今日は'+'曇りです')

print('''
これはPythonの練習です。
シングルクォーテーションを使っています。
             ''')
print("""
これはPythonの練習です。
ダブルクォーテーションを使っています。
             """)

#小数点以下が15桁
print(3.141592653589793)
#小数点以下が16桁
print(3.1415926535897932)

b = 20 > 10
b2 = 20 < 10

print(b)
print(b2)

a = 'あいうえお'
print(type(a))

#int型
b = 123
c = 2000
print(type(b))
print(type(c))

#float型
d = 450.75
e = 15.3678
print(type(d))
print(type(e))

#bool型
f = 10 > 1
g = 5 == 5
print(type(f))
print(type(g))

#int()関数で小数を整数に変換
print(int(1.2))
print(int(1.5))
print(int(1.55))

#int関数で文字列を整数に変換し、変数iに代入
i = int("2500")
print(i,'のデータ型は',type(i),'です。')

#文字列を小数に変換
print("125は:",float("125"))
#整数を小数に変換
print("34は:",float(34))
#True,Falseを小数に変換
print("Trueは:",float(True))
print("Falseは:",float(False))


#変数aに数値を代入
a = 12345
#変数aのデータ型を確認
print(type(a))
#変数aを文字列に変換し、データ型を確認
print(type(str(a)))

#様々な値を真偽値に変換

print(bool(15))
print(bool(-2))
print(bool('False'))
print(bool("False"))

print(bool(0))
print(bool(' '))
print(bool(" "))


a = 30 
b = 15

print(a,"+",b,"は",(a+b))
print(a,"-",b,"は",(a-b))
print(a,"×",b,"は",(a*b))
print(a,"÷",b,"は",(a/b))

a = 2.5
b = 3.5

print(a,"+",b,"は",(a+b))
print(a,"-",b,"は",(a-b))
print(a,"×",b,"は",(a*b))
print(a,"÷",b,"は",(a/b))

a = 'Hello'
b = 'World'
c = a * 2
print(a+b)
print(c)

a = "おいしい"
b = "夜ごはん"
c = a * 2
print(a+b)
print(c)

a = 'ありがとう'
b = "ございます"
c = a * 2
print(a+b)
print(c)

#文字列を変数sに代入
s = '100'
#数値を変数iに代入
i = 250
#変数sをint型に変換して計算
print(int(s)+i)
#変数iを文字列に変換して計算
print(s+str(i))


e = 'おはようございます'
e = 123
print(type(e))

f = '123'
print(int(f))


greeting = "こんばんは"
name = "小春"

print((greeting+name)*3)


num = 85
print('あなたの受付番号は'+str(num)+'です。')