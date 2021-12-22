#!/usr/bin/env python
# coding: utf-8
import win32com.client as win32
from tkinter import messagebox
import traceback
import tkinter
import time


def start_send_email(email_file_path, ever_view_zip_path):
    try:
        # 读取邮件文件
        email_files = open(email_file_path, 'r', encoding='UTF-8')
        email_file = email_files.read()
        email_files.close()
        email_file = email_file.split(';\n')

        print("开始发送邮件")
        # scheduled_time = datetime.datetime(2021, 12, 3, 17, 0, 0)
        # print('首次发送邮件的时间是：', scheduled_time)
        sysdate = time.strftime("%Y-%m-%d", time.localtime())
        outlook = win32.Dispatch('outlook.application')

        # 编辑邮件
        mail = outlook.CreateItem(0)
        mail.To = email_file[0]  # 收件人
        mail.CC = email_file[1]  # 抄送人
        mail.Subject = email_file[2]  # 邮件主题
        mail.Body = email_file[3]  # 邮件正文
        mail.Attachments.Add(ever_view_zip_path)  # 添加附件
        mail.Attachments.Add(r'C:\Users\zenazhang\Desktop\DWH_File.zip')#sql文件
        # mail.Importance = 2  # 设置重要性为高
        mail.Display()  # 显示发送邮件界面
        # mail.Send()  # 发送

        print("邮件发送成功")
    except Exception as e:
        print("save excel code is error")
        root = tkinter.Tk()
        root.withdraw()
        a = traceback.format_exc()
        messagebox.showinfo("save sql data is error", a)



