#!/usr/bin/env python
# coding: utf-8
from tkinter import messagebox
import pandas as pd
import traceback
import tkinter


def connect_sql_save_data(conn, sql_code, save_path, sheet_names: list) -> bool:

    try:
        sheet_s = []
        for name in sheet_names:
            if name != 'None':
                sheet_s.append(name)
        if len(sql_code) != len(sheet_s):
            print("The number of SQL statements is different from the number of names entered except None")
        with pd.ExcelWriter(save_path) as writer:
            for one_sql_code, name in zip(sql_code, sheet_s):
                data = pd.read_sql(one_sql_code, conn)
                data.to_excel(writer, sheet_name=name, index=False)
                # header=None
                print("SQL data save is Ture;")
        return True
    except Exception as e:
        print("save excel code is error")
        root = tkinter.Tk()
        root.withdraw()
        a = traceback.format_exc()
        messagebox.showinfo("save sql data is error", a)



