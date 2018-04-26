# 定义一个学生类
class Student():
    age = 18
    name = 'zaizai'

# 打印类的所有成员方法
print(Student.__dict__)

# 实例化类
jerry = Student()
print(jerry.name)


# 定义一个类
class A():
    name = 'dada'
    age = 100
    # self相当于this
    def getName(self):
        self.name = 'newName'
        self.age = 11
        return None

# 打印类的属性
print(A.name)
print(A.age)
print(id(A.name))
print(id(A.age))
print('*' * 20)

# 打印实例化类的属性
kaka = A()
print('查看实例化对象的属性')
print(kaka.__dict__)
print(kaka.name)
print(kaka.age)
print(id(kaka.name))
print(id(kaka.age))

'''
    结论：1、类A、实例化的对象kaka，name和age的id相同，初始化实例后kaka的——dict——为{}
         2、但是调用getName()后，kaka的——dict——为{'name': 'newName', 'age': 11}, 实例化对象kaka的name/age的id就发生了变化
'''


# 调用函数后，再重新调用
kaka.getName()
print('查看赋值后实例化对象的属性')
print(kaka.__dict__)
print(kaka.name)
print(kaka.age)
print(id(kaka.name))
print(id(kaka.age))

# self讲解
class SelfStudent():
    name = 'ni'
    age = 15
    # 定义方法
    def sayAge(self):
        # 直接打印age不能取到值，会报错
        # print('打印默认年龄是{0}'.format(age))
        self.age = 99
        print('打印self重新赋值后的年龄是{0}'.format(self.age))

mary = SelfStudent()

# 调用的时候，会把mary对象当成参数传给self, 即是self也可以写成其他单词
mary.sayAge()

# 例子2
# 定义类，不传self时
class Teacher():
    name = 'jok'
    age = 23
    def say(self):
        self.name = 'wang'
        self.age = 88
        print('打印self的name{0}'.format(self.name))
    # 不把self作为参数传入,可用__class__.name访问
    def sayAgain():
        print(__class__.name)
        print(__class__.age)
        print('测试不把self作为参数的结果')

# 实例化对象t
t = Teacher()

# 调用不传self就直接调用类的方法，会直接报错，self必须作为参数传入
# t.sayAgain()
# 可用下面方法调用
Teacher.sayAgain()

# 例子3
print('*' * 20 + '开始打印例子3的结果' + '*' * 20)
class A():
    name = 'lining'
    age = 55
    # 构建函数，初始化self
    def __init__(self):
        self.name = 'aaa'
        self.age = 20
    # 定义类方法
    def say(self):
        print('打印self的name--{0}'.format(self.name))
        print('打印self的age--{0}'.format(self.age))

class B():
    name = 'bbbb'
    age = 34

# 调用
a = A()
a.say()

# 采用类A直接调用时，需要传入参数作为self, 可以传入任意的参数
A.say(A)
A.say(a)
# 传入B时，就会打印class B的name 和 age
A.say(B)

print('*' * 20 + '开始打印例子4的结果' + '*' * 20)
# 例子4
# 定义私有变量：__age
class DemoFour():
    name = 'lili'
    # 定义私有变量
    __age = 50

d = DemoFour()
# name是公有变量，age是私有变量
print(d.name)

# 会报错，d没有__age属性
# print(d.__age)

# python的私有变量不是真私有，可以通过obj._classname__attributename, 如上文访问__age
print(d._DemoFour__age)
