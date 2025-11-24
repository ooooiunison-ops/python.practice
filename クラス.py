class Myclass:
    def class01(self):
        print((2+8)/2)
a = Myclass()
a.class01()

class person:
    def class02(self):
        print('私は{self.name}です。{self.age}才です。')

c=person()
c.name = '田中'
print(c.name)

class Number:

    def __init__(self):
        self.number=1
d=Number()
print(d.number)

class Math:
    def sum(self,x,y):
        print(x + y)
a= Math()
a.sum(12,14)

class Person:
    def __init__(self):
        self.name=''
        self.grade=''
a = Person()
a.name ='佐藤'
print(a.name,a.grade)

class Student:
    def score(self,math,science):
        print((math + science)/2)
c = Student()
c.score(65,55)

class Score:

    def __init__(self):
        self.name=''

    def sum(self,math,science,english):
        print(math + science + english)

d = Score()
d.name='阿部'
print(d.name)
d.sum(70,60,55)