# 例子1
########多继承的例子
class Fish():
    sex = '男'
    def __init__(self, name):
        self.name = name
        self.__age = 15
        self._school = '四川大学'
        self.firendly = True
    def swim(self):
        print('我会游泳')

class Bird():
    def __init__(self, name):
        self.name = name
        self.time = '2100221331'
    def fly(self):
        print('我会飞')

class Person():
    def __init__(self):
        self.sex = '男'
    def work(self):
        print('我会工作')


# 定义一个类，既可以游泳，也可以飞
class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name


s = SuperMan('周杰伦')
s.swim()
s.fly()
print(SuperMan.__dict__)
print(s.__dict__)
print(s.sex)
# 这里打印firendly、time属性报错的原因：
# 因为SuperMan中定义了构造函数，没有调用Bird以及Fish的构造函数__init__,所以定义在__init__中的self.属性不存在
# print(s.firendly)
# print(s.time)


# 例子2
################单继承的例子
class Student(Person):
    type = '学生'
    def test(self):
        Person.work(self)

s = Student()
s.test()
# 继承后并没有把父类的属性全部复制到子类上，而是子类只是通过某种方式调用
print(s.__dict__)
print(Student.__dict__)


# 例子3
#################菱形继承/钻石继承
class A():
    pass

class B(A):
    pass

class C(A):
    pass

# 此处D继承A，只会选择B继承的A
class D(B, C):
    pass

print(D.__mro__)


# 例子4
##################构造函数（魔法函数）
class Teacher():
    # 对Teacher类进行实例化操作的时候，最先调用的函数
    # name要确定
    # age要确定
    # addr要确定
    def __init__(self):
        self.name = '默认年龄'
        self.age = 22
        self.addr = '默认地址'

# 实例化的时候，初始化部分属性的函数，就叫构造函数（魔法函数）
t = Teacher()
print(t.__dict__)

# 例子4
#################构造函数的调用顺序

class A():
    def __init__(self):
        print('这是A类')

class B(A):
    def __init__(self, name):
        print('这是B类')
        print(name)

class C(B):
    # C中想扩展B的构造函数,B中已实现，不重复造轮子，C中不在实现
    # 即在调用B的构造函数后再添加一些功能
    # 由两种方法实现：
    '''
        # 1、先通过父类名调用，再添加自己的功能
        def __init__(self, name):
            # 先调用父类名称，调用父类的功能
            B.__init__(self, name)
            # 再添加自己的功能
            print('这是C中附加的功能')
    '''
    '''
        # 1、先通过super()调用，再添加自己的功能
        def __init__(self, name):
            # 先调用父类名称，调用父类的功能
            super(C, self).__init__(name)
            # 再添加自己的功能
            print('这是C中附加的功能')
    '''

# 实例化
c = C('我是C')


# 例子5
################多态Mixin设计模式

# 定义一个人类
class Person():
    name = 'jerry'
    age = 55

    def eat(self):
        print('人可以吃')

    def sleep(self):
        print('人可以睡')

# 定义老师类，老师除了吃、睡，还可以工作
class Teacher(Person):
    def work(self):
        print('老师可以工作')

# 定义学生类，学生除了吃、睡，还可以学习
class Student(Person):
    def study(self):
        print('学生可以学习')

# 定义助教类，既有老师的功能（教学），也有学生的功能（学习）
class Tutor(Teacher, Student):
    pass

t = Tutor()

print(Tutor.__mro__)
print(t.__dict__)

####################修改例子5，可以用mixin实现,Mixin不需要父类,只是表示一个单一功能
class TeacherMixin():
    def work(self):
        print('老师的mixin可以工作')

class StudentMixin():
    def study(self):
        print('学生的mixin可以学习')

class TutorM(Person, TeacherMixin, StudentMixin):
    pass

tt = TutorM()

print(tt.__dict__)
print(TutorM.__mro__)

# 检查是否是子类
print(issubclass(TutorM, Person))
# 检查对象是否是类的实例
print(isinstance(tt, TutorM))
# 检查一个对象是否有成员
print(hasattr(tt, 'name'))
print(hasattr(tt, 'addr'))
# 获取对象成员的属性
print(getattr(tt, 'name'))
# 获取成员列表
print(dir(tt))

# help(dir)
