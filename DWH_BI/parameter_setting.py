#!/usr/bin/env python
# coding: utf-8
import os
import tkinter
import datetime
import traceback
from tkinter import messagebox


def setting_pa():
    try:
        configuration_path = os.getcwd()
        configuration = open(configuration_path+'\\configuration_file.txt', 'r', encoding='UTF-8')
        configuration_file = configuration.read()
        configuration.close()
        configuration_list = configuration_file.split(';\n')
        # excel数据路径
        data_path = configuration_list[0]#C:\Users\zenazhang\PycharmProjects\pythonProject2\DWH_BI_Data\;

        # sql 语句路径
        sql_path = configuration_list[1]#C:\Users\zenazhang\PycharmProjects\pythonProject2\DWH_BI_Configure\Task.sql;

        # email 文件路径
        email_file_path = configuration_list[2]#C:\Users\zenazhang\PycharmProjects\pythonProject2\DWH_BI_Configure\email_file.txt;
        # sheet_names
        sheet_names = configuration_list[3]
        sheet_names = sheet_names.split(",")
        # 指定包excel路径
        package_configuration = configuration_list[4]
        run_time = str(datetime.datetime.now())
        run_time = run_time.split(" ")[0]

        view_path = configuration_list[5]
        ever_view_path = configuration_list[6]
        one_path = configuration_list[7]
        data_save_path = data_path+"dwh_excel_"+run_time+'.xlsx'
        view_save_path = view_path+"Statement_"+run_time+'.html'
        ever_view_zip_path = data_path+run_time+"_all_view.zip"
        print("parameter setting is True")
        return data_save_path, sql_path, sheet_names, email_file_path, package_configuration, view_save_path, ever_view_path, ever_view_zip_path, one_path, view_path

    except Exception as e:
        print("parameter setting  is error")
        a = traceback.format_exc()
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("parameter setting  is error", a)


