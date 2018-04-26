# 例子1
#############变量的3种用法
class A():
    def __init__(self):
        self.name = 'zaizai'
        self.age = 18
a = A()

# 属性的3种用法
# 1、赋值
# 2、读取
# 3、删除
a.name = '林语堂'
# print(a.name)

# 删除属性
del a.name
# print(a.name)

# 例子2
###############除了对变量的3中操作外，还想增加一些附加的操作，可以用property完成
class A():
    def __init__(self):
        self.name = '名字'
        self.age = 15

    # 此功能，是对类变量进行“读操作”的时候，执行的功能
    def fget(self):
        print('对变量进行读操作的时候，执行的功能')
        print(self.name)

    # 此功能，是对类变量进行“写操作”的时候，执行的功能
    def fset(self, name):
        print('对变量进行写操作的时候，执行的功能')
        self.name = name
        print(self.name)

    # 此功能，是对类变量进行“删除操作”的时候，执行的功能
    def fdel(self):
        print('对变量进行删除操作的时候，执行的功能')

    # 定义操作哪一个变量属性时，触发这些函数，name2属性
    name2 = property(fget, fset, fdel, '这是一个测试名字的例子')

a = A()
# print(a.name)
# 读操作
print(a.name2)
# 写操作
a.name2 = '这是name2名字'
# 删除操作
del a.name2


# 例子3
##################抽象方法
## 比如有一类方法，打招呼的方法，如果父类中定义了，对于狗是适用的，但对于人不适用
## 所有只是在父类中，定义一个抽象函数，用pass占位，再每一个子类中单独定义（类似于java中，在父类中只是定义好接口）

class Animal():
    def sayHello(self):
        # print('闻下对方的味道')
        pass

class Dog(Animal):
    def sayHello(self):
        print('闻一闻味道')

class Person(Animal):
    def sayHello(self):
        print('握一握手')

d = Dog()
d.sayHello()

p = Person()
p.sayHello()

# 例子4
####################抽象类的实现
import abc
# 声明一个类，并指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象的方法, 因为可能男、女不一样
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法,关键字不一样
    @abc.abstractclassmethod
    def drink(self):
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play(self):
        pass

    # 具体方法
    def sleep(self):
        print('sleeping')

# 例子5
################自己组装一个类(属性和方法的集合)
class B():
    pass

def say(self):
    print('say........')

B.say = say

b = B()
b.say()

#########第二种方法，引用types from MethodType
from types import  MethodType

class A():
    pass

def say(self):
    print('hi.............')

a = A()
a.say = MethodType(say, A)
a.say()


##########第三种方法，使用type()实现
def play(self):
    print('play..............')

# 使用type来创建一个类
A = type('AName', (object, ), {"class_say": play})

tt = A()
print(A.__dict__)
tt.class_say()


#########第四种方法，利用MetaClass()实现
# 元类写法固定
# 命名一般以MetaClass结尾
class TuLingMetaClass(type):
    # 注意以下写法
    def __new__(cls, name, bases, attrs):
        # 这里定义自己的业务逻辑
        print('%' * 20)
        print(cls)
        print(name)
        attrs['id'] = '000000'
        attrs['name'] = '北京海淀区公主坟西翠路12号'
        return type.__new__(cls, name, bases, attrs)

# 元类定义完就可以使用
class Teacher(object, metaclass=TuLingMetaClass):
    pass

t = Teacher()
print(t.__dict__)


















