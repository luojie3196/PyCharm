#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import json


class School(object):

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def create_class(self):
        print("欢迎创建班级".center(50, "-"))
        class_name = input("请输入班级名称：").strip()
        class_perod = input("请输入班级周期：").strip()
        class_obj = Classroom(class_name, school_obj.name, class_perod)
        classroom_dict[class_name] = class_obj
        class_obj.show_classroom_info()

    def hire_teacher(self):
        print("欢迎雇佣老师".center(50, "-"))
        t_name = input("请输入讲师名字：").strip()
        t_sex = input("请输入讲师性别：").strip()
        t_age = input("请输入讲师年龄：").strip()
        t_course = input("请输入讲师对应的课程：").strip()
        t_class = input("请输入讲师对应的班级：").strip()
        teacher_obj = Teacher(t_name, t_sex, t_age, t_course, t_class, school_obj.name)
        teachers_dict[t_name] = teacher_obj
        teachers_info = {"school_name": school_obj.name, "teacher_sex": t_sex,
                         "teacher_age": t_age, "teacher_course": t_course,
                         "teacher_class": t_class}
        teacher_obj.show_teacher_info()

        if not dic:
            dic[t_name] = teachers_info
            json.dump(dic, open("teacher_db", "w", encoding="utf-8"),
                      ensure_ascii=False, indent=2)
        else:
            if dic.get(t_name):
                print("[%s]讲师已经存在" % t_name)
            else:
                dic[t_name] = teachers_info
                json.dump(dic, open("teacher_db", "w", encoding="utf-8"),
                          ensure_ascii=False, indent=2)

    def create_course(self):
        print("欢迎创建课程".center(50, "-"))
        c_type = input("请输入课程类型：").strip()
        c_name = input("请输入课程名称：").strip()
        c_price = input("请输入课程价格：").strip()
        c_period = input("请输入课程周期：").strip()
        course_obj = Course(c_type, c_name, c_price, c_period, school_obj.name)
        courses_dict[c_name] = course_obj
        course_obj.show_course_info()


class Course(object):

    def __init__(self, course_type, course_name, course_price, course_period, course_place):
        self.course_type = course_type
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period
        self.course_place = course_place

    def show_course_info(self):
        print("""
        -----------[%s]课程信息------------
        Name:%s
        type:%s
        price:%s
        period:%s
        """ % (self.course_name, self.course_name, self.course_type,
               self.course_price, self.course_period))


class Classroom(object):

    def __init__(self, c_name, c_school_name, c_period):
        self.c_name = c_name
        self.c_school_name = c_school_name
        self.c_period = c_period

    def show_classroom_info(self):
        print("""
        Name:%s
        Period:%s
        """ % (self.c_name, self.c_period))


class SchoolMember(object):

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


class Student(SchoolMember):

    def __init__(self, name, sex, age, stu_school, stu_id, stu_course, course_price):
        super(Student, self).__init__(name, sex, age)
        self.stu_id = stu_id
        self.stu_course = stu_course
        self.course_price = course_price
        self.stu_school = stu_school

    def show_student_info(self):
        print("""
        -------------[%s]学生信息---------------
        Name:%s
        School:%s
        Sex:%s
        Age:%s
        ID:%s
        Course:%s
        Course price:%s
        """ % (self.name, self.name, self.stu_school, self.sex,
               self.age, self.stu_id, self.stu_course, self.course_price))


class Teacher(SchoolMember):

    def __init__(self, name, sex, age, course, classroom, school_name):
        super(Teacher, self).__init__(name, sex, age)
        self.course = course
        self.classroom = classroom
        self.school_name = school_name

    def show_teacher_info(self):
        print("""
        -------------[%s]讲师信息--------------
        Name:%s
        Sex:%s
        Age:%s
        Course:%s
        Classroom:%s
        School Name:%s
        """ % (self.name, self.name, self.sex, self.age,
               self.course, self.classroom, self.school_name))

    def show_classroom(self, te_name):
        class_room = Classroom(teachers_dict[te_name].classroom,
                               courses_dict[teachers_dict[te_name].course].period,
                               school_obj.name)
        class_room.show_classroom_info()

    def show_student(self):
        stu_name = input("请输入要查看学生名字：").strip()
        stu_dict[stu_name].show_student_info()


def stu_register():
    stu_name = input("请输入学生名字：").strip()
    stu_sex = input("请输入学生性别：").strip()
    stu_age = input("请输入学生年龄：").strip()
    stu_id = input("请输入学生ID：").strip()
    print("1.%s[%sRMB], 2.%s[%sRMB], 3.%s[%sRMB], 4.返回" % (c1.course_name, c1.course_price,
                                                           c2.course_name, c2.course_price,
                                                           c3.course_name, c3.course_price))
    while True:
        num = input("请选择课程：").strip()
        if num == "1":
            stu_course = c1.course_name
            stu1 = Student(stu_name, stu_sex, stu_age, school_obj.name,
                           stu_id, stu_course, c1.course_price)
            stu_dict[stu_name] = stu1
            break
        elif num == "2":
            stu_course = c2.course_name
            stu1 = Student(stu_name, stu_sex, stu_age, school_obj.name,
                           stu_id, stu_course, c2.course_price)
            stu_dict[stu_name] = stu1
            break
        elif num == "3":
            stu_course = c3.course_name
            stu1 = Student(stu_name, stu_sex, stu_age, school_obj.name,
                           stu_id, stu_course, c3.course_price)
            stu_dict[stu_name] = stu1
            break
        elif num == "4":
            break
        else:
            continue
    stu1.show_student_info()


def students_view():
    while True:
        print("1.注册\n"
              "2.返回\n"
              "3.退出")
        num = input("请选择：").strip()
        if num == "1":
            stu_register()
        elif num == "2":
            break
        elif num == "3":
            sys.exit()
        else:
            continue

def teacher_view():
    name = input("请输入教师姓名：").strip()
    while True:
        if teachers_dict.get(name):
            print("欢迎[%s]讲师".center(50, "-") % name)
        else:
            print("[%s]讲师不存在".center(50, "-") % name)
            break
        print("1.查看班级\n"
              "2.查看学员信息\n"
              "3.返回\n"
              "4.退出")
        num = input("请选择：").strip()
        if num == "1":
            teachers_dict[name].show_classroom(name)
        elif num == "2":
            teachers_dict[name].show_student()
        elif num == "3":
            break
        elif num == "4":
            sys.exit()
        else:
            continue


def school_view():
    while True:
        print("1.创建班级\n"
              "2.创建课程\n"
              "3.雇佣讲师\n"
              "4.返回")
        num = input("请选择：").strip()
        if num == "1":
            school_obj.create_class()
        elif num == "2":
            school_obj.create_course()
        elif num == "3":
            school_obj.hire_teacher()
        elif num == "4":
            break
        else:
            continue


def main():
    global dic
    global school_obj
    dic = {}
    while True:
        print("请选择学校".center(50, "*"))
        choice = input("1.%s, 2.%s, 3.返回 4.退出" % (s1.name, s2.name)).strip()
        if choice == "1":
            school_obj = s1
        elif choice == "2":
            school_obj = s2
        elif choice == "3":
            break
        elif choice == "4":
            sys.exit()
        else:
            continue
    while True:
        print("1.学校管理视图\n"
              "2.讲师视图\n"
              "3.学员视图\n"
              "4.返回\n"
              "5.退出")
        num = input("请选择视图：").strip()

        if num == "1":
            print("欢迎进入学校管理视图".center(50, "*"))
            school_view()
        elif num == "2":
            print("欢迎进入讲师视图".center(50, "*"))
            teacher_view()
        elif num == "3":
            print("欢迎进入学员视图".center(50, "*"))
            students_view()
        elif num == "4":
            break
        elif num == "5":
            sys.exit()
        else:
            continue

if __name__ == '__main__':
    teachers_dict = {}
    courses_dict = {}
    classroom_dict = {}
    stu_dict = {}
    s1 = School("Old boy", "beijing")
    s2 = School("IT center", "shanghai")
    c1 = Course("IT", "Linux", "12000", "1 year", "beijing")
    c2 = Course("IT", "Python", "22000", "8 month", "beijing")
    c3 = Course("IT", "Go", "20000", "8 month", "shanghai")
    courses_dict["Linux"] = c1
    courses_dict["Python"] = c2
    courses_dict["Go"] = c3
    t1 = Teacher("Alex", "M", "38", "Python", "S13", "Old boy")
    t2 = Teacher("Cheng", "M", "35", "Linux", "S15", "Old boy")
    teachers_dict["Alex"] = t1
    teachers_dict["Cheng"] = t2
    print(s1, s2)
    main()




