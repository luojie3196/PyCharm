#!/usr/bin/python
# -*- coning:utf-8 -*-

import re
import pymysql


def get_repo_local(manifest):
    f1 = None
    try:
        f1 = open(manifest, 'r')
    except IOError:
        print('Error:')
    finally:
        if f1:
            f1.close()
    file_list =  f1.readlines()

    reg = r'project name="(.*?)" path="(.*?)" revision="(.*?)"'
    pattern = re.compile(reg)
    path_list = re.findall(pattern, str(file_list))
    reg1 = r'project groups="(.*?)" name="(.*?)" path="(.*?)" revision="(.*?)"'
    pattern1 = re.compile(reg1)
    path_list1 = re.findall(pattern1, str(file_list))

    for group, lLocal,rLocal, branch in path_list1:
        path_list.append((lLocal, rLocal, branch))
    return path_list
# print zip(*pathList)

# remote_path local_path branch
def insert_data(proj, repo_info):
    conn = pymysql.connect(host = 'localhost', user = 'root', password = '93560', db = 'db_int', port = 3306)
    cur = conn.cursor()
    query = "insert into repository(project, remote_path, local_path, branch) value('" + proj + "', %s, %s, %s)"
    print(query)
    cur.executemany(query, repo_info)
    cur.close()
    conn.close()


# local_path branch remote_path
def update_data(proj, repo_info):
    conn = pymysql.connect(host = 'localhost', user = 'root', password = '93560', db = 'db_int', port = 3306)
    cur = conn.cursor()
    query = "update repository set local_path = %s branch = %s where remote_path = %s and project = '" + proj + "'"
    print(query)
    cur.executemany(query, repo_info)
    cur.close()
    conn.close()


def check_data(proj, repo_info):
    conn = pymysql.connect(host = 'localhost', user = 'root', password = '93560', db = 'db_int', port = 3306)
    cur = conn.cursor()
    query = "select * from repository where project = '%s'" % proj
    cur.execute(query)
    db_data = cur.fetchall()
    cur.close()
    conn.close()
    # print alldata
    insert_list = []
    update_list = []
    db_list = []
    num = 0
    num1 = 0

    for id, project, branch, remote_path, local_path, comment in db_data:
        db_list.append((remote_path, local_path, branch))

    for line in repo_info:
        if line in db_list:
            # print 'Exist: ', line
            num += 1
            continue
        print('Not Exist: ', line)
        insert_list.append(line)
        num1 += 1
    print(len(db_list))
    print(num)
    print(num1)
    if update_list:
        print('update_list')
        print(update_list)
        # update_data(proj, update_list)
    if insert_list:
        print('insert_list')
        print(insert_list)
        insert_data(proj, insert_list)


project = 'mercury_custo'
repo_info = get_repo_local('default.xml')

check_data(project, repo_info)