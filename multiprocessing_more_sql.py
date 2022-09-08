#!/usr/bin/env python
# coding: utf-8
import pymssql
import datetime
import multiprocessing


def sql_connection1(step):
    #
    connect_file = open(r'cs.txt', 'r', encoding='UTF-8')
    connect = connect_file.read()
    connect_file.close()
    connect = connect.split(";")
    s_time = datetime.datetime.now()

    conn = pymssql.connect(host=connect[0], user=connect[1],
                           password=connect[2], database=connect[3],
                           charset="utf8")
    cur = conn.cursor()
    if conn:
        # print("sql sever is connect Ture")
        e_time = datetime.datetime.now()
        sql_file = open(r'test.sql', 'r', encoding='UTF-8')
        sql = sql_file.read()
        sql = sql.split(";")
        cur.execute(str(sql[0]))
        row = cur.fetchone()
        with open(r'log.txt', "a", encoding='UTF-8') as file:
            file.write(str(e_time - s_time)+'\n')
            # file.write(" \n \n \n " + str(s_time) + '************* 开始连接数据库时间: ' + '用户' + str(step)
            #            + '\n ' + str(e_time) + "************* 连接数据库成功时间: " + '用户' + str(step)
            #            + '\n ' + str(e_time - s_time) + '连接数据库完成花费时间: ' + '用户' + str(step)
            #            + '\n ' + '数据库查询结果: #################################################### \n' + str(row[0:5])
            #            + '\n ' + '#################################################################  \n \n  '
            #            )
    else:
        with open(r'log.txt', "a", encoding='UTF-8') as file:
            file.write('\n' + "connect sql sever is error" + '用户' + str(step))


if __name__ == "__main__":
    multiprocessing.freeze_support()

    pool = multiprocessing.Pool(processes=60)
    for i in range(60):
        pool.apply_async(sql_connection1, (i,))
    pool.close()
    pool.join()

