#!/usr/bin/env python
# coding: utf-8
import connect_sql
import read_sql
import save_sql_data
import view_first_half
import view_second_half
import save_view
import send_email
import parameter_setting
import traceback
import send_email_to_manager
import zip_view
import os
"""
使用此模块需要先修改配置文件：configuration_file.txt 和 sql_connect.txt 文件保存位置为此模块本地位置，请勿移动。

配置文件内容：

注意事项：每行以  ;(英文分号)换行  结束，最后一行  不用使用;(英文分号)  结尾
注意事项：每行以  ;(英文分号)换行  结束，最后一行  不用使用;(英文分号)  结尾

第一行：sql数据保存为excel的位置(为文件夹路径)

第二行：运行的sql文件位置(文件路径)
                     (sql内容注意事项：每个sql语句  以;(英文分号)换行  结束，最后一行不用使用  ;(英文分号)   结尾)
                            
第三行：需要发送的邮件内容
                     (注意事项：每部分 以;(英文分号)换行结束，最后一行不用使用;(英文分号)结尾 ，文档格式与邮件格式相同
                      第一部分：收件人邮箱 ;
                      第二部分：抄送人邮箱 ;
                      第三部分：主题内容;
                      第四部分：正文内容)

第四行：数据保存为excel后的表名
                     (注意事项：由于可视化获取数据为指定表名获取，故设置默认共8个表名，当不使用某一个表时可以将此表名设为None）

第五行：指定包的excel的路径
model：
    dwh_main model : 主模块(需要运行的模块)分别调用各个子模块
    parameter_setting model :各个模块默认参数和输入参数设置
    connect_sql model :连接数据库模块
    read_sql model: 读取sql语句文件模块
    save_sql_data model: 使用sql语句从sql获取数据保存
    view_first_half 和 view_second_half  model:可视化模块
    save_view  model: 可视化保存模块
    send_email  model: 邮件发送模块
       
# sql文档要以;加换行结尾
# 邮件文档要按收件人、抄送人、主题、正文顺序排序并每个内容以;与换行结束。
第六行：总html路径
第七行：每个子html路径
第八行：每个子html路径的相对路径
"""
# 连接数据库组件


def main():
    try:
        conn = connect_sql.con_sql()
        # 导入参数组件
        data_save_path, sql_path, sheet_names, email_file_path, excel_configuration, view_save_path, ever_path, ever_view_zip_path, one_path, view_path = parameter_setting.setting_pa()
        if os.path.exists(ever_path) is False:
            os.mkdir(ever_path)
        # 读取sql组件
        sql_code = read_sql.sql_read_file(sql_path, excel_configuration)

        # 导出sql数据为excel表
        save_sql_data.connect_sql_save_data(conn, sql_code, data_save_path, sheet_names)

        # 可视化
        view_first_half.weekly_and_monthly(data_save_path, sheet_names[0:2], ever_path)
        view_second_half.bar_time_wave(data_save_path, sheet_names[2], ever_path)
        view_second_half.bar_count_wave(data_save_path, sheet_names[3], ever_path)
        view_first_half.Top_Time(data_save_path, sheet_names[4], ever_path)
        view_first_half.Top_Counts(data_save_path, sheet_names[5], ever_path)
        view_second_half.funnel_error_week(data_save_path, sheet_names[6], ever_path)
        view_second_half.funnel_error_all(data_save_path, sheet_names[7], ever_path)
        save_view.write(view_save_path, one_path)
        # 邮件
        zip_view.getZipDir(view_path, ever_view_zip_path)
        send_email.start_send_email(email_file_path, ever_view_zip_path)

    except Exception as e:
        print("send email to manager")
        error = traceback.format_exc()
        print(error)
        send_email_to_manager.send_error(error)



