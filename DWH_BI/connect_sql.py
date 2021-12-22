#!/usr/bin/env python
# coding: utf-8
import pymssql
import traceback
import tkinter
from tkinter import messagebox
import os


def con_sql():
    try:
        connect_file_path = os.getcwd()
        connect_file = open(connect_file_path + '\\sql_connect.txt', 'r', encoding='UTF-8')
        connect = connect_file.read()
        connect_file.close()
        connect = connect.split(",")
        conn = pymssql.connect(connect[0], connect[1], connect[2], connect[3], charset='utf8')
        if conn:
            print("sql sever is connect Ture")
        return conn
    except Exception as e:
        print("connect sql sever is error")
        a = traceback.format_exc()
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("connect_sql_error", a)

