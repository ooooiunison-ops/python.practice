class Student:

    def __init__(self,name):
        self.name = name
    
    def __del__(self):
        print('DELETE!!')

person = Student('Yamamoto')
print(person.name)
del person
print('--------')

class Greeting1:
    def say_morning(self):
        print('おはよう')

class Greeting2(Greeting1):
    pass

japanese_greeting = Greeting2()
japanese_greeting.say_morning()

class Besis:
    def attak(self):
        print('攻撃')
class fighter(Besis):
    pass
#インスタンスを作成する
Fighter_action = fighter()
#親クラスが持っていたattakメソッドを実行
Fighter_action.attak()

class Greeting1:
    def say_morning(self):
        print('おはよう')
class Greeting2:
    def say_hello(self):
        print('こんにちは')
class Greeting3(Greeting1,Greeting2):
    pass
japanese_greeting = Greeting3()
japanese_greeting.say_morning()
japanese_greeting.say_hello()

class Wizard:
    def spell(self):
        print('呪文')
class Fighter:
    def ability(self):
        print('特技')
class Superman(Wizard,Fighter):
    pass
#インスタンスを作成
superman_action = Superman()
#親クラスが持っていたspellメソッドを実行
superman_action.spell()
#親クラスが持っていたabilityメソッドを実行
superman_action.ability()

class Besis():
    def attack(self):
        print('攻撃')
class Fighter(Besis):
    def attack(self):
        print('拳で攻撃')

fighter_action = Fighter()
fighter_action.attack()

class Greeting:
    def say_morning(self):
        print('おはよう')
class E_Greeting(Greeting):
    def say_morning(self):
        print('Good Morning')
#インスタンスを作成する
english_greeting=E_Greeting()
#上書きしたメソッドを実行する
english_greeting.say_morning()

class Dog1:
    def __init__(self,name,age):
        self.name =name
        self.age =age
class Dog2(Dog1):
    def __init__(self,name,age):
        self.name =name
        self.age =age
        print(self.name,self.age)

profile_dog2 = Dog2('shibako',2)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Japanese(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        print(self.name,self.age)
#引数'太郎'と15を渡してインスタンスを作成する
japanese_person =Japanese('太郎',15)

class MyClass:
    my_variable = 'This is a class variable'
    print(my_variable)


class dog:
    spacies = 'Canis familiaris'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    print(spacies)

class Age:
    class_age = 12
    def __init__(self,age):
        self.age = age
    @classmethod
    def increment_age(cls):
        cls.class_age += 1
        return cls.class_age
print(Age.increment_age())
print(Age.increment_age())

class division:
    a = 60
    b = 12
    
    @staticmethod
    def add():
        return division.a/division.b
print(division.add())

class Teacher:
    def __init__(self,school):
        self.school= 'school'
        
    def __del__(self):
        print('DELETE!!')

perple = Teacher('Tanaka')
print(perple.school)
del perple
print('--------')

class Student:
    def math(self,score):
        print(score)
class Grade1(Student):
    def English(self,score):
        print(score)

studentA = Student()
studentB = Grade1()
studentA.math(20)
studentB.math(30)
studentB.English(40)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Grade1(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        print(self.name)
        print(self.age)
person1=Grade1('Sasayama',20)

class Koushi:
    job ='junior high school koushi'
    age = 13
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
koushiA = Koushi('Yamanoi',20)
print(koushiA.job)
print(koushiA.name)
print(koushiA.age)

koushiB = Koushi('Sakuma',16)
print(koushiB.job)
print(koushiB.name)
print(koushiB.age)

class instructor:
    job ='junior high school koushi'
    age = 14
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def add_age(cls):
        cls.age += 1
        return cls.age
print(instructor.add_age()) 