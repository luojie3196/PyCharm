#!/usr/bin/python
# -*- coding:utf-8 -*-


class Role(object):

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print('shoting...')

    def got_shot(self):
        print('ah..., I got shot...')

    def buy_gun(self, gun_name):
        print('%s just bought %s' %(self.name, gun_name))

r1 = Role('Alex', 'Police', 'AK47')
r2 = Role('Jack', 'terrorist', 'B22')
r1.buy_gun('AK47')
r1.got_shot()
