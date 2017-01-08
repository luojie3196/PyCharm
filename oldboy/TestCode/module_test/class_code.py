#!/usr/bin/python
# -*- coding:utf-8 -*-

import time


class School(object):

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self, stu_obj):
        print('Enrolling for %s student' % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print('Hire new staff %s' % staff_obj.name)
        self.staffs.append(staff_obj)


class SchoolMember(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

    # def enroll(self):
    #     SchoolMember.members += 1
    #     print('New member [%s] is enrolled, now there are [%s] members now.' % (self.name, SchoolMember.members))
    #
    # def __del__(self):
    #     print('member [%s] is dead.' %self.name)


class Teacher(SchoolMember):

    def __init__(self, name, age, sex, course, salary):
        super(Teacher, self).__init__(name, age, sex)
        self.course = course
        self.salary = salary

    def teach(self):
        print('[%s] is teaching [%s] course.' % (self.name, self.course))

    def tell(self):
        msg = '''
        ----info of teacher %s ----
        Name: %s
        Age: %s
        Sex: %s
        Salary: %s
        Course: %s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course)
        print(msg)


class Student(SchoolMember):

    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.grade = grade
        self.stu_id =stu_id

    def tell(self):
        msg = '''
        ----info of student %s ----
        Name: %s
        Age: %s
        Sex: %s
        Stu_id: %s
        Grade: %s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade)
        print(msg)

    def pay_tuition(self, amount):
        print('%s has paid tuition for $%s' % (self.name, amount))


school = School('Oldboy IT', 'BJ')

t1 = Teacher('Oldboy', 56, 'M', 2000000, 'Linux')
t2 = Teacher('Alex', 22, 'M', 3000, 'PythonDevOps')

s1 = Student('Roger', 28, 'M', 1001, 'PythonDevOps')
s2 = Student('Logolove', 20, 'M', 1002, 'Linux')

t1.tell()
s1.tell()


school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.staffs)
school.staffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)