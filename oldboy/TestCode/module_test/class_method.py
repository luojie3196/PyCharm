#!/usr/bin/python
# -*- coding:utf-8 -*-


# class Dog(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def eat(self):
#         print('%s is eating...' % self.name)
#
# d = Dog('Jack')
# d.eat(d)


# class Dog(object):
#
#     def __init__(self, name):
#         self.name = name
#
      # '''通过@staticmethod装饰器即可把其装饰的方法变为一个静态方法,是不可以访问实例变量或类变量的，
      # 一个不能访问实例变量和类变量的方法，其实相当于跟类本身已经没什么关系了，它与类唯一的关联就是需要
      # 通过类名来调用这个方法。'''
#     @staticmethod
#     def eat(name, food):
#         print('%s is eating %s...' % (name, food))
#
# d = Dog('Jack')
# d.eat('Alex', 'Baozi')


# class Dog(object):
#     name = 'dog'
#     food = 'Baozi'
#
#     def __init__(self, name):
#         self.name = name
#
#     # 类方法通过@classmethod装饰器实现，类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
#     @classmethod
#     def eat(cls):
#         print('%s is eating %s...' % (cls.name, cls.food))
#
# d = Dog('Jack')
# d.eat()


class Dog(object):
    name = 'dog'
    food = 'Baozi'

    def __init__(self, name, food):
        self.name = name
        self.food = food

    # 属性方法的作用就是通过@property把一个方法变成一个静态属性
    @property
    def eat(self):
        print('%s is eating %s...' % (self.name, self.food))

d = Dog('Jack', 'Mantou')
d.eat
