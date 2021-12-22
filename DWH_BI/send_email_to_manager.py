#!/usr/bin/env python
# coding: utf-8
import win32com.client as win32


def send_error(error):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = "zenazhang@deloitte.com.cn"  # 收件人
    mail.CC = "vjiang@deloitte.com.cn"  # 抄送人
    mail.Subject = "Task error"  # 邮件主题
    mail.Body = "Dear Zenas,this is error: "+error  # 邮件正文
    mail.Importance = 2  # 设置重要性为高
    mail.Display()  # 显示发送邮件界面
    mail.Send()  # 发送
