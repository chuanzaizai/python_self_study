# 例子1
#############类的属性描述
# 创建Student类，描述学生类
# 学生具有Student.name属性
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 自动调用大写函数
        self.setName(name)

    # 介绍下自己
    def introduce(self):
        print('你好，我叫{0}，我今年{1}岁'.format(self.name, self.age))

    # 第一种方法：定义一个方法，来过滤用户输入的name
    def setName(self, name):
        self.name = name.upper()

    # 第二种方法：运用属性方法property()，来过滤用户输入的name(例子2)



# 正常情况下，姓名的大小写不规范，需要定义一套规则，来过滤/验证姓名的规则
s = Student('LIU Ming', 26)
s.introduce()

s1 = Student('michi stangle', 26)
s1.introduce()


#例子2
######################property()方法来定义、过滤属性name和age
# name要求全部大写
# age必须是整数

class Person():
    '''
        这里是说明文档
    '''
    # 函数的名称可以任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        # 输入的姓名以大写保存
        self._name = name.upper()

    def fdel(self):
        self._name = 'NoName'

    name = property(fget, fset, fdel, '对name操作完成了')

# 实例化
p1 = Person()
p1.name = 'tuling'
# 打印说明文档
print(Person.__doc__)
# 父类, 元组，只有一个元素，后面要叫逗号
print(Person.__bases__)
print(p1.name)
print(p1._name)

# 例子3
#################魔术函数不需要人为调用
class A():
    def __init__(self, name=0):
        print('__init__()被自动调用了')

a = A()

# __call__()方法：
class B():
    def __init__(self):
        print('__init__被调用了')
    # call方法
    def __call__(self, *args, **kwargs):
        print('__call__方法被调用了')
        print('**' * 20)
        print(args)
        print(kwargs)
        for i in args:
            print(i)
        for k,v in kwargs.items():
            print(k, '--->', v)

# 实例化
b = B()

# 实例化对象b当成函数调用
b('22', '四川成都', sex='男', school='电子科技大学')


# __str__()方法
class C():
    def __init__(self):
        print('__init__被调用了')
    # str方法
    def __str__(self):
        print('__str__被调用了')
        return '这是__str__的返回值'

c = C()
# 打印的时候，会调用__str__方法
print(c)


# __getattr__()方法
class D():
    name = 'zaizai'
    def __init__(self):
        print('init被调用了')
    def __getattr__(self, name):
        print(name)
        return '这里是返回值'
d = D()
print(d.name)
print('********')
# 访问不存在的attr属性时触发__getattr__方法
print(d.attr)


# __setattr__方法
class E():
    def __init__(self):
        print('__init__调用成功')
    # key: 属性名
    # value： 属性值
    def __setattr__(self, key, value):
        print('设置属性: {0}'.format(key))
        # 下面的语句会导致，死循环, 因为对自己赋值
        # self.key = value
        # 应该调用super,调用父类的属性方法，修改父类的属性，进而子类的属性就该了
        super().__setattr__(key, value)

e = E()
e.age = 18


# 例子4
##################__gt__()进行大于判断时触发
class Student():
    def __init__(self, score):
        score = int(score)
        self._score = score

    # __gt__方法
    def __gt__(self, obj):
        print('哈哈，{0}大于{1}吗？'.format(self._score, obj._score))
        return self._score > obj._score

s1 = Student(50)
s2 = Student(88)

print(s1 > s2)

# 例子5
################实例方法、静态方法、类方法
class Person():
    # 实例方法
    def eat(self):
        print('实例方法')

    # 类方法classmethod
    # 类方法第一个参数，一般命名为cls，区别self
    # 需要用@classmethod声明,可以访问类属性
    @classmethod
    def play(cls):
        print('类方法')

    # 静态方法staticmethod
    # 不需要yoga第一个参数表示自身或者类
    # 需要用@staticmethod声明,不能访问类属性，不能访问self
    @staticmethod
    def say():
        print('静态方法')


yue = Person()

# 实例方法
# 如果不实例化，就要传入参数，表示self
# Person.eat(Person)
yue.eat()
# 类方法
Person.play()
yue.play()
# 静态方法
Person.say()
yue.say()





