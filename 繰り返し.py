a = 'apple'
for i in a :
    print(i)

for i in range(0,20,3):
    print(i)

for i in range(5):
    print('Good morning')

i = 0
j = 0

while i < 6 or j < 11:
    print(i,j)
    i += 1
    j += 2

x = (10,20,30,40,50)
i = 0

while i < len(x):
    print(x[i])
    i += 1

i = 0
while i < 10:

    if i == 5:
        break
    print(i)
    i += 1

i = 0
while i < 6:
    if i == 4:
       i += 1
       continue
    print(i)
    i += 1

i = 0
j = 0

while i < 4 or j < 7:
    print(i,j)
    i += 1
    j += 2

else:
    print('繰り返し処理が正常に行われました')

for i in range(1,8,2):
    for j in range(1,8,2):
        print(f'i={i},j={j}')

i = 0
while i < 3:
    j = 0
    while j < 10:
        print(f'i = {i},j = {j}')
        j += 3
    i += 1

for i in range(1,15,2):
    print(i)

i = 0
j = 0
while i < 10 and j < 20:
    print(i,j)
    i += 1
    j += 2

a = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(a):
    if a[i]%2 == 0:
        i += 1
        continue
    print(a[i])
    i += 1

a = ['Hat','Clothes','Pants']
b = ['red','blue','yellow']
for i in a:
    for j in b:
        print(f'{i} : {j}')

i = 100
while True:
    print(i)
    i *= 2
    if i >= 100:
        break
print('無限ループを抜けました')