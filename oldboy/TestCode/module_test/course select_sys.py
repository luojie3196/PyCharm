#!/usr/bin/python
# -*- coding:utf-8 -*-


class School(object):

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course = []
        self.grade = []

    def create_course(self, obj):
        print('[%s] created [%s] course' % (self.name, obj.name))
        self.course.append(obj)

    def create_grade(self, obj):
        print('[%s] created [%s] grade' % (self.name, obj.name))
        self.grade.append(obj)


class Student(object):

    def __init__(self, name, school_obj):
        self.name = name
        self.school = school_obj

    def enroll(self):
        pass

    def pay_tuition(self):
        pass

    def select_grade(self):
        pass


class Teacher(object):

    def __init__(self, name, school_obj):
        self.name = name
        self.school = school_obj

    def select_grade(self):
        pass

    def show_stu_info(self):
        pass

    def change_stu_score(self):
        pass


class Course(object):

    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price


class Class_t(object):

    def __init__(self, name, course_obj, teacher_obj):
        self.name = name
        self.course = course_obj
        self.teacher = teacher_obj

school_bj = School('Oldboy IT', 'Beijing')
school_sh = School('Oldboy IT', 'Shanghai')

cour_python = Course('Python', 6, 15000)
cour_linux = Course('Linux', 4, 12000)
cour_go = Course('Go', 4, 10000)

t1 = Teacher('Alex', school_bj)
t2 = Teacher('Jack', school_bj)
t3 = Teacher('Mike', school_sh)

school_bj.create_course(cour_linux)
school_bj.create_course(cour_python)
school_sh.create_course(cour_go)

c1 = Class_t('python class one', cour_python, t1)
c2 = Class_t('Linux class one', cour_linux, t2)
c3 = Class_t('Go class one', cour_go, t3)

school_bj.create_grade(c1)
school_bj.create_grade(c2)
school_sh.create_grade(c3)

s1 = Student('Roger', school_bj)
s2 = Student('Logove', school_sh)
