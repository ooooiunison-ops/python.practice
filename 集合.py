x = {0.3,11,(10,20,30),0.3,'Python'}
print(x)

x = 'apple'
print(set(x))

x = set()
x.add('peach')
print(x)

x = {'cat','dog','bird'}
x.remove('dog')
print(x)

x = {0.1,0.003,0.5,7}
x.pop()
print(x)

x = {'red','blue','yellow'}
x.clear()
print(x)

a={1,2,3}
b={2,3,4}
c={3,4,5}
d = a|b|c
print(d)

a = {1,3,5}
b = {7,5,9}
a |= b
print(a)

a = {0,2,5}
b = {9,5,0}
c = {0,5,9}
d = a & b & c
print(d)

x = {1,2,3}
y = {5,4,3}
z = x - y
print(z)

x = {3,6,9}
y = {0,3,6}
x -= y
print(x)

x = {4,2,8}
y = {0,4,2}
z = x ^ y
print(z)

x = {0.5,'apple',20,(1,2)}
print((1,2) in x)
print(10 in x)

x = {0.3,'peach',10,100}
for i in x:
    print(i)

a = ['cat','dog','bird']
print(set(a))

x = {'Mike','Bob'}
x.add('Aria')
print(x)

x = {1,10,100,1000}
x.remove(100)
print(x)

a = {0.1,'apple',10}
b = [1,'peach',10]
c = (5,'banana',10)
d = a.intersection(b,c)
print(d)

x ={'blue',100,0.5,1}
print(0.5 in x)
print('red' in x)