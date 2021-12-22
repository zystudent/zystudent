#!/usr/bin/env python
# coding: utf-8
import plotly as py
# import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd
pio.templates.default = "plotly_white"
pylt = py.offline.plot


def weekly_and_monthly(file_path, sheet_names, view_path):
    data1_1 = pd.read_excel(file_path, sheet_name=sheet_names[0])

    date1_1 = data1_1["date_day"].values.tolist()
    time1_1 = data1_1["Daily_execution_time"].values.tolist()
    y1_1 = []
    # x1_1 = []

    for i in time1_1:
        y1_1.append(round(i / 3600, 2))
    y1_11 = []
    for i in time1_1:
        second = i
        m, s = divmod(second, 60)
        h, m = divmod(m, 60)
        y1_11.append("%02d:%02d:%02d" % (h, m, s))
    data1_2 = pd.read_excel(file_path, sheet_name=sheet_names[1])
    # print(data1_2)

    date1_2 = data1_2["date_day"].values.tolist()
    time1_2 = data1_2["Daily_execution_time"].values.tolist()
    y1_2 = []
    # x1_2 = []
    for i in time1_2:
        y1_2.append(round(i / 3600, 2))
    y1_22 = []
    for i in time1_2:
        second = i
        m, s = divmod(second, 60)
        h, m = divmod(m, 60)
        y1_22.append("%02d:%02d:%02d" % (h, m, s))
    week_fig = go.Scatter(x=date1_1, y=time1_1, text=y1_11,
                          line_shape='spline', marker_size=10, marker_color="rgb(177,195,210)")
    month_fig = go.Scatter(x=date1_2, y=time1_2, text=y1_22,
                           line_shape='linear', marker_size=10, marker_color="rgb(177,195,210)")
    layoutnew = list(
        [dict(
            # type="buttons"
            direction="right"
            , active=0
            , x=0.6
            , y=1.134
            , buttons=list(
                [dict(label="Week"
                      , method="update"
                      , args=[{"visible": [True, False]}
                        , {'showlegend': False}]),
                 dict(label="Month"
                      , method="update"
                      , args=[{"visible": [False, True]}
                         , {'showlegend': False}])
                 ])
        )]
    )
    layout = dict(title=dict(text="Time Trend", x=0.5), showlegend=False, updatemenus=layoutnew)
    datanew = [week_fig, month_fig]
    fignew = go.Figure(data=datanew, layout=layout)
    return pylt(fignew, filename=view_path+'weekly_and_monthly.html', auto_open=False)


def Top_Counts(file_path, sheet_names, view_path):
    data4 = pd.read_excel(file_path, sheet_name=sheet_names)
    name4 = data4["PACKAGE_NAME"].values.tolist()
    counts4 = data4["COUNTS"].values.tolist()

    y4 = []
    for i in counts4:
        y4.append(round(i / 1000000, 2))
    layout4 = go.Layout(title=dict(text="Total Counts Top%d" %(len(name4)), x=0.5),
                        xaxis=dict(title='Package Name'),
                        yaxis=dict(title='Counts(million)'))
    fig4 = go.Figure(go.Bar(x=name4, y=y4, text=y4, textposition="outside", marker_color="#9AC0CD"),
                     layout=layout4)  # B4CDCD

    return pylt(fig4, filename=view_path+'Top_Counts.html', auto_open=False)


def Top_Time(file_path, sheet_names, view_path):
    data5 = pd.read_excel(file_path, sheet_name=sheet_names)
    name5 = data5["PACKAGE_NAME"].values.tolist()
    time5 = data5["Total_Times"].values.tolist()
    # print(name5,time5)
    y5 = []
    y5_1 = []
    for i in time5:
        y5_1.append(round(i / 3600, 1))
        # print(time5)
    # print(y5_1)#转成小时
    for i in time5:
        second = i
        m, s = divmod(second, 60)
        h, m = divmod(m, 60)
        y5.append("%02d:%02d:%02d" % (h, m, s))
    layout5 = go.Layout(title=dict(text="Total Time Consuming Top%d" %(len(name5)), x=0.5),
                        xaxis=dict(title='Package Name'),
                        yaxis=dict(title='Time Consuming(S)'))
    fig5 = go.Figure(go.Bar(x=name5, y=time5, text=y5, marker_color="#9AC0CD", textposition="outside"),
                     layout=layout5, )
    return pylt(fig5, filename=view_path+'Top_Time.html', auto_open=False)

