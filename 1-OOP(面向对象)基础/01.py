'''
    定义一个学生类，用来形容学生
'''

# 定义一个空的类
class Student():
    # 定义空类，pass防止语法报错
    pass

# 定义一个对象
jay = Student()

# 定义一个类，描述听python的学生
class PythonStudent():
    # 学生姓名
    name = None
    age = 18
    course = 'python'
    # 注意事项：
    # 1、函数末尾添加return None
    # 2、注意缩进层级
    # 3、系统默认的self参数
    def doHomeWork(self):
        print('做作业')
        print('我在zhph-001分支上面改了一个东西')
        return None

# 实例化一个具体的学生:mary
mary = PythonStudent()
print(mary.name)
print(mary.age)
# 未传入参数
mary.doHomeWork()

# 查看一个类的所有属性
print(PythonStudent.__dict__)



