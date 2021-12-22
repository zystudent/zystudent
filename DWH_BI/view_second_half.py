#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly as py
from time import gmtime
from time import strftime
pylt = py.offline.plot
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
go.layout.template = "plotly_white"


# Task2 view
def bar_time_wave(data_save_path, sheet_names, view_path):

    time_wave = pd.read_excel(data_save_path,sheet_name=sheet_names)
    time = []
    for i in time_wave['time_standard_deviation'].tolist():
        seconds = i
        time.append(strftime("%H:%M:%S", gmtime(seconds)))
    time_h = time_wave['time_standard_deviation'] / 3600

    pyplot = py.offline.plot
    time = go.Bar(x=time_wave['PACKAGE_NAME'], y=time_wave['time_standard_deviation']
                  , marker=dict(color='#104E8B')
                  , opacity=0.39
                  , text=time,
                  textposition="outside"
                  )
    layout = go.Layout(title=dict(text="Load Time Consum Wave Top10", x=0.5)
                       , yaxis=dict(title="Time_Consum(s)")
                       , template="plotly_white"
                       , xaxis=dict(
            rangeslider=dict(
                visible=True),

        )
                       )
    figure_time_wave = go.Figure(data=time, layout=layout)
    load_time_wave = pyplot(figure_time_wave, image_height=1600, image_width=1600,
                            filename=view_path+'time_wave.html', auto_open=False)
    return load_time_wave


# Task3 View
def bar_count_wave(data_save_path, sheet_names, view_path):
    count_wave = pd.read_excel(data_save_path, sheet_name=sheet_names)
    pyplot = py.offline.plot
    count = go.Bar(x=count_wave['load_standard_deviation'].sort_values(ascending=True), y=count_wave['PACKAGE_NAME']
                   , marker=dict(color='#36648B')
                   , opacity=0.39
                   , orientation='h'
                   )
    layout = go.Layout(title=dict(text="Load Time Consum Wave Top10", x=0.5)
                       , xaxis=dict(title="Load_Count")
                       , template="plotly_white"
                       , yaxis=dict(
            title="PACKAGE_NAME",
        )
                       )

    figure_count_wave = go.Figure(data=count, layout=layout)
    # figure.update_traces(textposition="outside")
    load_count_wave=pyplot(figure_count_wave, image_height=1600, image_width=1600,
                           filename=view_path+'count_wave.html', auto_open=False)
    return load_count_wave
    # Task6_week


def funnel_error_week(data_save_path, sheet_names, view_path):

    error_week = pd.read_excel(data_save_path, sheet_name=sheet_names)
    pyplot = py.offline.plot
    error_week = go.Funnel(
        x=error_week['Week_Error_reporting_rate'],
        y=error_week['PACKAGE_NAME'].tolist(), textposition="inside", textinfo="value+percent initial",
        texttemplatesrc='outside', marker=dict(color='#B4CDCD'))
    layout = go.Layout(title=dict(text="Error Rate This Week Top10", x=0.5)
                       , xaxis=dict(title="Error_Rate(k)")
                       , yaxis=dict(title="PACKAGE_NAME")
                       # ,yaxis_tickangle=30#坐标轴倾斜
                       # ,width=1000
                       # ,height=800
                       , template="plotly_white"
                       )
    figure_error_week = go.Figure(data=error_week, layout=layout)
    error_rate_week = pyplot(figure_error_week, filename=view_path+'error_week.html', auto_open=False)
    return error_rate_week


def funnel_error_all(data_save_path, sheet_names, view_path):

    error_all = pd.read_excel(data_save_path,sheet_name=sheet_names)
    pyplot = py.offline.plot
    error_all = go.Funnel(
        x=error_all['Error_reporting_rate'],
        y=error_all['PACKAGE_NAME'].tolist(), textposition="inside", textinfo="value+percent initial",
        texttemplatesrc='outside', marker=dict(color='#A2B5CD'))
    layout = go.Layout(title=dict(text="Error Rate Since Record Top10", x=0.5)
                       , xaxis=dict(title="Error_Rate(k)")
                       , yaxis=dict(title="PACKAGE_NAME")
                       # ,width=1000
                       # ,height=800
                       , template="plotly_white"
                       )
    figure_error_records = go.Figure(data=error_all, layout=layout)
    return pyplot(figure_error_records, filename=view_path+'error_all.html', auto_open=False)
