age = 19
if age>=18:
    print('成年')

age = 14
if age>=18:
    print('成年')
else:
    print('未成年')

age = 6
if age>= 18:
    print('成年')
elif 6<=age<=12:
    print('小学生')
elif 13<=age<=15:
    print('中学生')
else :
    print('未成年')

number = 16
if number % 2 == 0 and number % 3 ==0:
    print('6の倍数です')
elif number % 2 == 0 and number % 3 !=0:
    print('2の倍数です')
elif number % 2 != 0 and number % 3 ==0:
    print('3の倍数です')
else:
    print('2と3の倍数ではありません')


fruits = 'cherry'
match fruits:
    case'apple':
        print('りんご')
    case'orange':
        print('みかん')
    case'cherry':
        print('さくらんぼ')
    case'grape':
        print('ぶどう')
    case _:
        print('その他の果物')

age = 16
if age >= 18:
    print('成年')
else :
    pass

age = 18
print('成年' if age>=18 else '未成年')

a = 123
if type(a)is int:
    print('整数型です')
elif type(a)is str:
    print('文字列型です')
elif type(a)is float:
    print('小数点型です')
elif type(a)is bool:
    print('ブール型です')
elif type(a)is list:
    print('リスト型です')
elif type(a)is tuple:
    print('タプル型です')
elif type(a)is dict:
    print('辞書型です')
else:
    pass

age = 21
if age >= 18:
    print('成年')

age = 15
if age >= 18:
    print('成年')
else:
    print('未成年')

age = 15
if age >= 18:
    print('成年')
elif 6<= age <= 12:
    print('小学生')
elif 13<= age <= 15:
    print('中学生')
else:
    print('未成年')

number = 21
if number % 2 == 0 and number % 3 == 0:
    print('6の倍数です')
elif number % 2 == 0 and number % 3 != 0:
    print('2の倍数です')
elif number % 2 != 0 and number % 3 == 0:
    print('3の倍数です')
else :
    print('2と3の倍数ではありません')

age = 17
print('成年' if age >= 18 else '未成年')