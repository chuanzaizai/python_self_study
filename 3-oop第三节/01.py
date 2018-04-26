print('*' * 20 + '开始打印例子1的结果' + '*' * 20)
# 例子1
# 定义一个person类（父类）
# Person有工作的函数，Teacher也有工作的函数，Teacher的工作就是对Person的补充
class Person():
    name = '父类'
    age = 15
    # 定义受保护的属性“小名”，子类可以用，不能公用
    _petname = '言'
    # 定义考试成绩, 只能自己访问
    __score = 0
    def sleep(self):
        print('人类都会睡觉')
        return None

# 定义一个老师类，Teacher是person的子类
# person写在括号内表明：teacher是person的子类
class Teacher(Person):
    # 定义子类特有的属性
    teacher_id = '2011221331'
    # 定义和父类相同的属性name，则优先使用子类的
    name = '子类'
    def makeTest(self):
        print('老师可以考试')
        return None
    # 扩充父类函数的方法
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        Person.sleep(self)
        # 扩充父类的另一种方法,super代表得到父类
        print(super())
        super().sleep()
        # 调用同级方法
        self.makeTest()


# 实例化
t = Teacher()

t.work()

# 打印实例t + 类Teacher的属性
# print(t.name)
# print(Teacher.age)
# print(t._petname)
# 会报错，__score是私有属性
# print(t.__score)

# Person(父类)并没有将并没有将name,age等属性赋值到Teacher(子类)中，而Teacher(子类)只是通过引用关系调用Person(父类)的属性和方法
# 可以用id()方法来验证
# print(Teacher.__dict__)

# 例子2
#############构造函数
class Dog():
    # 语法： __init__就是构造函数
    # 每次实例化，第一个被调用，被自动执行
    # 主要工作：进行初始化
    def __init__(self, name):
        print('这就是构造函数')
        print(name)

# 实例化的时候，括号内的参数应该和__init__的参数匹配
kaka = Dog('名字')

###############继承中的构造函数（动物-->宠物-->狗）
# 动物类
class Animal():
    pass

# 宠物类
class Pet(Animal):
    def __init__(self):
        print('宠物继承了动物类')
# 定义狗
class Dog(Pet):
    def __init__(self):
        print('这只狗继承了宠物类')

# 定义猫，猫没有构造函数,会调用父类的构造函数，一级一级向上查找，知道找到为止
class Cat(Pet):
    pass

# 不会调用父类的构造函数
zaizai = Dog()

# 实例化猫，会一层一层向上查找父类的构造函数
anan = Cat()

# 例子3
##############__mro__解决继承树的层级问题
class Root():
    pass

class A(Root):
    pass

class B(Root):
    pass

class Child(A, B):
    name = '子类'
    pass

# 打印Child的继承树
# 结果未：Child --> A --> B --> Root
print(Child.__mro__)
print(Child.__dict__)