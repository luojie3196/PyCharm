#!/usr/bin/python
# encoding:utf-8


class Foo(object):
    '''Foo class used to test some spec ways'''
    def func(self):
        pass

print(Foo.__doc__)

# __doc__ 表示类的描述信息
# __module__ 表示当前操作的对象在哪个模块
# __class__  表示当前操作的对象的类是什么
# __call__ 对象后面加括号，触发执行(构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()())
# __dict__ 查看类或对象中的所有成员
# __str__ 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值
# 用于索引操作，如字典。以上分别表示获取、设置、删除数据
class Foo(object):
    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']  # 自动触发执行 __getitem__
obj['k2'] = 'alex'  # 自动触发执行 __setitem__
del obj['k1']

# 类默认是由 type 类实例化产生
# 类的生成 调用 顺序依次是 __new__ --> __call__ --> __init__
def func(self):
    print("hello %s"%self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age
Foo = type('Foo',(object,),{'func':func,'__init__':__init__})

f = Foo("jack",22)
f.func()

# 反射
# 通过字符串映射或修改程序运行时的状态、属性、方法
class Foo(object):
    def __init__(self):
        self.name = 'wupeiqi'
    def func(self):
        return 'func'
obj = Foo()
# #### 检查是否含有成员 ####
hasattr(obj, 'name')
hasattr(obj, 'func')
# #### 获取成员 ####
getattr(obj, 'name')
getattr(obj, 'func')
# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)
# #### 删除成员 ####
delattr(obj, 'name')
delattr(obj, 'func')

# 动态导入模块
import importlib
__import__('import_lib.metaclass')  # 这是解释器自己内部用的
# importlib.import_module('import_lib.metaclass') #与上面这句效果一样，官方建议用这个


