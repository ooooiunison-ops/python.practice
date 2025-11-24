#リスト作成
numbers = [1,2,3,4,5,6]
#リスト内包表記を使用してリストnum2に数値を追加
num2 = [i**2 for i in numbers]

print(num2)

#集合を生成
s = {'りんご',100,'apple'}
#リスト内包表記でリストを生成
list = [i for i in s]
print(list)

#辞書を作成
dic = {'a':'apple','b':'banana','c':'orange'}
#リスト内包表記でリストを生成
list = [i for i in dic]
list2 = [i for i in dic.keys()]
list3 = [i for i in dic.values()]
list4 = [i for i in dic.items()]

print('通常:',list)
print('keys():',list2)
print('values():',list3)
print('items():',list4)

#集合を作成
s ={1,2,3,4,5}
#集合内包表記で新しい集合を作成
syugou = {i*5 for i in s}
print(syugou)

#リストを作成
l1 = {200,400,600,800}
#集合内包表記で新しい集合を作成
s = {i/5 for i in l1}
print(s)


#辞書を作成
dic = {1:'うさぎ',2:'ハムスター',3:'モルモット'}
#集合内包表記で集合を作成
s1 = {i for i in dic}
s2 = {i for i in dic.keys()}
s3 = {i for i in dic.values()}
s4 = {i for i in dic.items()}

print('通常:',s1)
print('keys():',s2)
print('values():',s3)
print('items():',s4)

#リストを作成
num = {1,2,3,4,5}
#辞書内包表記で辞書を生成
d = {i*2:i*3 for i in num}
print(d)

#集合を作成
s = {100,200,300,400}
#辞書内包表記で辞書を作成
dic ={i:i*2 for i in s}
print(dic)


#要素が奇数の場合、要素を2倍にした値を格納
List1 = [i*2 for i in range(1,11) if 1%2 == 1]
print(List1)

a = ['ウサギ','トラ','ゾウ','アライグマ','ペンギン']
new_a = [i if 'ウ' in i else 'ウを含まない動物' for i in a]
print(new_a)

l1 = [1,2,3]
l2 = [1,10,100]
#内容表記のネスト
result =[i * j for i in l1 for j in l2]
print(result)

#練習１
num = [1,2,3,4,5]
double_num = []
for i in num :
    double_num.append(i*2)
print(double_num)

num = [1,2,3,4,5]
double_num = [i*2 for i in num]
print(double_num)

d = {'apple':100,'bread':200,'cheese':300}
new_s1 = [i for i in d.keys()]
new_s2 = [i for i in d.items()]
print(new_s1)
print(new_s2)

L = [150,250,350,450]
new_d ={i*2:i*4 for i in L}
print(new_d)


animals = ['fox','cat','rabbit','penguin','bear']
new_a = []
for i in animals:
    if 'a' in i:
        new_a.append(i)
    else :
        new_a.append(len(i))
print(new_a)

animals = ['fox','cat','rabbit','penguin','bear']
new_a =[i if 'a' in i else len(i) for i in animals]
print(new_a)

list1 = [1,2,3]
list2 = ['a','b','c']

new_list = [x*y for x in list1 for y in list2]
print(new_list)