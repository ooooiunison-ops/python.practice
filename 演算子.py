#算術演算子
print(4 + 2)
print(4 - 2)
print(4 * 2)
print(4 / 2)
print(4 % 2)
print(4 ** 2)

x = 9
y = 6
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)

print(10 > 8)
print(10 < 8)
print(10 >= 8)
print(10 <= 8)
print(10 == 8)
print(10 != 8)

x = 8
y = 5
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

x =[1, 2, 3]
y =[1, 2, 3]
z = x

print(x is y)
print(x is z)

x =[1, 2, 3]
y =[1, 2, 3]
z = x

print(id(x))
print(id(y))
print(id(z))

x =[4, 5, 6]
y =[4, 5, 6]
z = x

print(x is not y)
print(x is not z)

x = [1, 2, 3]
y = ['東京','大阪','福岡']

print(6 in x)
print('東京'in y)

x = [4, 5, 6]
y = ['apple','peach','grape']

print(6 not in x)
print('banana' not in y)

x = 10
y = 5

print(x > 6 and x == 12)
print(y >= 7 or y < 14)

x = 9
y = 13
z = 20

x += 11
z -= y
print(x)
print(z)

print(bin(1))
print(bin(3))
print(bin(5))


c = 0b0101
d = 0b0111
e = c & d
print(bin(e))

x = 0b0101
y = 0b0111
z = x | y
print(bin(z))


a = 0b0101
b = 0b0111
c = a ^ b
print(bin(c))

x = 0b1101

a = x >> 1
b = x << 3
print(bin(a))
print(bin(b))

x = 10
x += 10
print(x)

x = 14
y = 22
y += x
print(x)
print(y)

x = 20
y = 4
z = 20

print(x <= y)
print(x >= z)

x = 10
y = 5
print(x==5 or y==5)
print(x==1 or y==1)

print(bin(4))
print(bin(9))
print(bin(15))