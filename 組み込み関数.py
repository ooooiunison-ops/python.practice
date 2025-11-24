a = ['abe','kimura','sato']

print(a)
print(type(a))
print(len(a))

print(bool(5>2))

a = tuple(['SQL','Python','VBA'])
print(a)
b = dict(name = 'ueda',age = 17)
print(b)

print(float(10))
print(round(1.43))

b = [2,4,6,8]
print(sum(b))
print(max(b))
print(min(b))


print(range(7))
c = ['sato','tanaka','takahashi']
d = [14,18,19]
print(zip(c,d))
print(enumerate(c))

print('apple','grape','orange',sep='-')

print('Hello world',end='!!!')

number = [10,20,30,40,50,60]
a = slice(0,5,2)
print(number[a])

print(divmod(29,7))
print(pow(2,3))
print(pow(2,3,5))

number = (3)
def my_func(number):
    print('この変数のデータ型は',type(number))
    if type(number) is int:
        print('引数を３で割った結果が',divmod(number,3))
        print('引数を２乗した結果が',pow(number,2))
    elif type(number) is float:
        print('引数をまとめると',round(number))

def my_type(text):
    if type(text) is str:
        print('引数の文字数は',len(text))
        print('引数の最大値は',max(text))
        print('引数の最小値は',min(text))
        a = slice(1,4,2)
        print('作成したスライスオブジェクトは',text[a])        
my_func(5)
my_func(2.1)
my_type('abcdef')