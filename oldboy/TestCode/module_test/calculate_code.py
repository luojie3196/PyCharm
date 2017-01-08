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
    DEBUG and print('minus_f:', res.group(1), res.group(2))
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


def bracket_calc(input_t):
    while ('/' in input_t) or ('*' in input_t):
        res = re.findall(r'\d*\.?\d*[*/]-*\d*\.?\d*', input_t)
        DEBUG and print('bracket_calc:', res[0])
        input_t = input_t.replace(res[0], arithmetic(res[0]))
    DEBUG and print('bracket_calc-1:', input_t)
    input_t = input_t.replace('+-', '-').replace('--', '+').replace('-+', '-')
    while not is_number(input_t):
        if input_t.startswith('-'):
            res = re.match(r'-\d+\.?\d*[+-]\d*\.?\d*', input_t)
        else:
            res = re.match(r'\d+\.?\d*[+-]\d*\.?\d*', input_t)
        DEBUG and print('bracket_calc-2:', res)
        val = res.group(0)
        input_t = input_t.replace(val, arithmetic(val))
        DEBUG and time.sleep(1)
    return input_t


def main(input_t):
    input_t = input_t.replace(' ', '')
    while '(' in input_t:
        res = re.search(r'.*(\([+\-*/0-9.]+\)).*', input_t)
        input_res = res.group(1)
        DEBUG and print('main: ', input_res)
        new_input = input_res.strip('(').strip(')').replace(' ', '')
        DEBUG and print('main-1: ', new_input)
        val = bracket_calc(new_input)
        DEBUG and print('main-2:', val)
        input_t = input_t.replace(input_res, val)
        input_t = input_t.replace('+-', '-').replace('--', '+').replace('-+', '-')
    DEBUG and print('main-3: ', input_t)
    result = bracket_calc(input_t)
    return result


# input_t = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
input_t = input('Please input expression: ')
result = main(input_t)
print(result)