#!/usr/bin/python
# -*- coding:utf-8 -*-


class Animal(object):

    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Cat(Animal):

    def talk(self):
        print('Miao...!')


class Dog(Animal):

    def talk(self):
        print('Ao Ao...!')


c1 = Cat('cat')
d1 = Dog('dog')

Animal.animal_talk(c1)
Animal.animal_talk(d1)