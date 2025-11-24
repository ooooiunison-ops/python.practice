a = ['リンゴ','イチゴ','バナナ']
print(a)

a = [
    ['たろう','じろう','さぶろう'],
    ['はなこ','みちこ','よしこ'],
    ['けん','しん','そう'],
    ]
print(a)

a = ['sato','suzuki','takahashi']
b =a+['tanaka','watanabe']
print(b)

a = ['sato','suzuki','takahashi']*2
print(a)

subject=['国語','算数','英語','社会','理科']
print(subject[4])

subject=['国語','算数','英語','社会','理科']
print(subject[-2])

drink=['water','tea','juice']
print('tea' in drink)

drink=['water','tea','juice']
print('coffee' in drink)

sweets = ['candy','chocolate','candy','cookies','candy']
print(sweets.count('candy'))

prefectures = ('Tokyo','Osaka','Hokkaido')
print(prefectures.index('Hokkaido'))

number = [470,0,8750,50,100,999,1]
number.sort()
print(number)

number = [0,50,51,808,90,888,965]
number.sort(reverse=True)
print(number)

word = 'こんにちは'
word01 = list(word)
print(type(word01))

print(list(range(7)))

number = (0,1,87,50,142,583)
print(sorted(number))

people = ['James','Emily','Michael']
people.insert(0,'Sarah')
print(people)

sports = ['soccer','basketball','tennis','baseball']
sports.append('swimming')
print(sports)

food = ['pizza','sushi','burger']
food.remove('sushi')
print(food)

Month = ['January','February','March']
Month.clear()
print(Month)

a = [1,2,3]
a.append(4)
print(a)