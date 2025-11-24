text = 'Python'
print(len(text))
print(id(text))

import datetime
print(datetime.datetime.now())

import datetime
dt = datetime.datetime(2025,1,1)
print(dt - datetime.timedelta(days = 10))

import random
print(random.randint(1,10))

def greeting():
    print('Hello Python')
greeting()

txt = 'Hello Python'
def len_test():
    return print(len(txt))
len_test()

txt = 'Hello Python'
def id_test(txt):
    return(id(txt))
print(id_test(txt))

import random
def random_type():
    number = random.randint(10,20)
    print(number)
    print(type(number))
random_type()

import random
import datetime
def today_meal():
    meal = random.randint(1,10)
    print(meal)
    return(meal)

def diet():
    if meal == 6:
        print('鶏むね肉と温野菜')
    elif meal == 7:
        print('一色プロテインに置き換え')
    elif meal == 8:
        print('我慢しよう')
    elif meal == 9:
        print('サラダ')
    elif meal == 10:
        dietday= datetime.datetime.now()
        dietday= dietday+ datetime.timedelta(days=1)
        print('やっぱり',dietday,'から！')
meal = today_meal()

match meal:
    case (1):
        print('今日はラーメン')
    case (2):
        print('今日は蕎麦')
    case (3):
        print('今日はうどん')
    case (4):
        print('今日はパスタ')
    case (5):
        print('今日は白米')
    case _ :
        print('ダイエット')
        diet()