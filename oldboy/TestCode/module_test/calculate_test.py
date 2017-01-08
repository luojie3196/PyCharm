#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
import time

DEBUG = False

def add_f(num):
    res = re.search(r'(-*\d*\.?\d*)\s*\+\s*(\d*\.?\d*)', num)
    sum_t = float(res.group(1)) + float(res.group(2))
    return sum_t


def minus_f(num):
    res = re.search(r'(\d*\.?\d*)\s*-\s*(\d*\.?\d*)', num)
    DEBUG and print('minus: ', res.group(1), res.group(2))
    if res.group(1):
        minus_t = float(res.group(1)) - float(res.group(2))
    else:
        minus_t = 0 - float(res.group(2))
    return minus_t


def multip_f(num):
    res = re.search(r'(\d*\.?\d*)\s*\*\s*([+-]*\d*\.?\d*)', num)
    multip_t = float(res.group(1)) * float(res.group(2))
    return multip_t


def division_f(num):
    res = re.search(r'(\d*\.?\d*)\s*/\s*(\d*\.?\d*)', num)
    division_t = float(res.group(1)) / float(res.group(2))
    return division_t


def arithmetic(new_input):
    if '+' in new_input:
        cal_res = add_f(new_input)
    elif '*' in new_input:
        cal_res = multip_f(new_input)
    elif '/' in new_input:
        cal_res = division_f(new_input)
    elif '-' in new_input:
        cal_res = minus_f(new_input)
    else:
        cal_res = int(new_input)
    return str(cal_res)


def complex_calc(input_t):
    if '(' in input_t:
        res = re.search(r'.*(\([+\-*/0-9]+\)).*', input_t)
        input_res = res.group(1)
        new_input = input_res.strip('(').strip(')')
        while True:
            if '+' in new_input:
                cal_res = add_f(new_input)
            elif '-' in new_input:
                cal_res = minus_f(new_input)
            elif '*' in new_input:
                cal_res = multip_f(new_input)
            elif '/' in new_input:
                cal_res = division_f(new_input)
            else:
                result = int(new_input)
                break
            DEBUG and time.sleep(1)
            if input_res:
                new_input = input_t.replace(input_res, str(cal_res))
                input_res = None
                continue
            new_input = str(cal_res)
    else:
        result = arithmetic(input_t)
    return result


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# (1 + 2*3 - 5 + 3/3 )
# 9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14
def bracket_calc(input_t):
    while ('/' in input_t) or ('*' in input_t):
        res = re.findall(r'\d*\.?\d*[*/]-*\d*\.?\d*', input_t)
        DEBUG and print('aaaaaaaaa:', res[0])
    # if res:
    #     for n in res:
            # print(n)
        input_t = input_t.replace(res[0], arithmetic(res[0]))
    DEBUG and print('666666:', input_t)
    input_t = input_t.replace('+-', '-').replace('--', '+').replace('-+', '-')
    while not is_number(input_t):
        if input_t.startswith('-'):
            res = re.match(r'-\d+\.?\d*[+-]\d*\.?\d*', input_t)
        else:
            res = re.match(r'\d+\.?\d*[+-]\d*\.?\d*', input_t)
        DEBUG and print('res:', res)
        val = res.group(0)
        input_t = input_t.replace(val, arithmetic(val))
        DEBUG and time.sleep(1)
    return input_t
# (1 + 2) * 5

# input_t = input('Please input("q" exit):').strip()
# input_t = input('Please input("q" exit):').replace(' ', '')

#(1 + 2*3)
# while True:
# input_t = '20 + (1.1 + 2*3.5 -5 + 3/3 + 5 + 2*8) + 10'.replace(' ', '')
# input_t = '(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )'.replace(' ', '')
input_t = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'.replace(' ', '')
# if '(' in input_t:
while '(' in input_t:
    res = re.search(r'.*(\([+\-*/0-9.]+\)).*', input_t)
    input_res = res.group(1)
    DEBUG and print('input_res: ', input_res)
# input_res = '(1 + 2*3 -5 + 3/3 )'
    new_input = input_res.strip('(').strip(')').replace(' ', '')
# simple_calc(input_t)
    DEBUG and print('222: ', new_input)
    val = bracket_calc(new_input)
    DEBUG and print('val:', val)
    input_t = input_t.replace(input_res, val)
    input_t = input_t.replace('+-', '-').replace('--', '+').replace('-+', '-')
DEBUG and print('111: ', input_t)
result = bracket_calc(input_t)
print(result)

