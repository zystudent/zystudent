#!/usr/bin/env python
# coding: utf-8
import traceback


def write(view_save_path, one_path):
    try:
        f = open(view_save_path, 'w')
        str1 = one_path+'weekly_and_monthly.html'
        str2 = one_path+'time_wave.html'
        str3 = one_path+'count_wave.html'
        str4 = one_path+'Top_Counts.html'
        str5 = one_path+'Top_Time.html'
        str6 = one_path+'error_week.html'
        str7 = one_path+'error_all.html'
        message = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>DWH Statement</title>
        <style>
        body{
        margin:0;
        padding:0;
        }
        div {
    
        width=1600px;
        }
        h1 {
    
        display:block;
        text-align:center;
        }
    
        </style>
        </head>
        <body >
        <h1 >DWH Statement</h1>
        <div >
        <iframe src=%s width="1500px" height="740px" name="周趋势图" frameborder="0" ></iframe>
        <iframe src=%s width="1500px" height="740px" name="周趋势图" frameborder="0" ></iframe>
        <iframe src=%s width="1500px" height="740px" name="周趋势图" frameborder="0" ></iframe>
        <iframe src=%s width="1500px" height="740px" name="周趋势图" frameborder="0" ></iframe>
        <iframe src=%s width="1500px" height="740px" name="周趋势图" frameborder="0" ></iframe>
        <iframe src=%s width="1500px" height="740px" name="周趋势图" frameborder="0" ></iframe>
        <iframe src=%s width="1500px" height="740px" name="周趋势图" frameborder="0" ></iframe>
    
        </div>
        </body>
    
    
        </html>
        """ % (str1, str2, str3, str4, str5, str6, str7)
        f.write(message)
    except Exception as e:
        print("send email to manager")
        error = traceback.format_exc()
        # send_email_to_manager.send_error(error)
