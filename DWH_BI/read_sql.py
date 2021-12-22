#!/usr/bin/env python
# coding: utf-8
from tkinter import messagebox
import pandas as pd
import traceback
import tkinter


def sql_read_file(file_sql, excel_configuration) -> list:
    # Open and read the file as a single buffer
    try:
        fd = open(file_sql, 'r', encoding='UTF-8')
        sql_file = fd.read()
        fd.close()
        sql_code = sql_file.split(';\n')

        excel_data = pd.read_excel(excel_configuration)  # 默认读取到Excel的第一个表单
        pd_excel_data = pd.DataFrame(excel_data)
        package_name = pd_excel_data['PACKAGE_NAME']
        if len(package_name) != 0:
            a = "'',''".join(package_name)
            b = "'''" + a + "'''"
            sql_code[0] = sql_code[0]+b
            sql_code[1] = sql_code[1]+b
        print("read sql file is Ture")
        return sql_code

    except Exception as e:
        print("read file split is error")
        a = traceback.format_exc()
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("read sql is error", a)


