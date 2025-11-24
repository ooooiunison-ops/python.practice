#変数の指定と初期化
a = 123
name = 'Tanaka'

#変数を利用
print(a)
print(a,name)

#代入
a = 15
b = a
a = 25

print(a)
print(b)

a = 'Satou'
b = a
a = 'Itou'

print(a)
print(b)

A_1 = 123
_B1 = 456

print(A_1)
print(_B1)

#大文字と小文字の区別
A = 10
a = 20

#変数の参照
print(A)
print(a)

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

#予約語の使用


A = 100
print (id(A))
B = A
A = 200
print (id(A))
print (id(B))



A = 10
B = 10.0

#AはBである
print(A is B)
#AはBではない
print(A is not B)


A = 1
B = 10
print(A)
print(B)

C = 1234
D = 'TANAKA'
print(C)
print(D)

a = 3.14
A = 1592
print(a)
print(A)

A = 30
B = A
A = 40
print(A)
print(B)

A = 50
B = A
A = 200
print(id(A))
print(id(B))

A = 100
B = 200
print(A)
print(B)
print(A)
print(B)

A = 30
B = 40
print(A is B)
print(A is not B)