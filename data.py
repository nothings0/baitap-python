import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
with open("data.csv", encoding="utf8") as file:
    data = file.read().split("\n")
def type_1(df, plt):
    grouped_2 = df.groupby('year')["pr"].sum()
    grouped_2.plot(kind="bar", x="Năm")
    plt.ylim(0, 2500)
    plt.ylabel("Lượng mưa")
    plt.title("Lượng mưa trung bình từ 2010 - 2015")
    plt.show()
def type_2(df, plt):
    grouped_1 = df.groupby('year')["temp"].mean()
    grouped_1.plot(kind="bar", x="Năm")
    plt.ylim(0, 30)
    plt.ylabel("Nhiệt độ")
    plt.title("Nhiệt độ trung bình từ 2010 - 2015")
    plt.show()
def type_3(df, plt):
    for i in range(len(data)):
        data[i] = data[i].split(',')
    header = data[0]
    data_core = data[1:]
    df = pd.DataFrame(data_core, columns=header)
    year_arr = ["2010", "2011", "2012", "2013", "2014", "2015"]
    month_arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    arr = []
    for i in range(len(year_arr)):
        g = df.groupby("year").get_group(year_arr[i])["pr"].tolist()
        arr_2 = [float(i) for i in g]
        arr.append(arr_2)
    
    plt.plot(month_arr, arr[0], label = "2010")
    plt.plot(month_arr, arr[1], label = "2011")
    plt.plot(month_arr, arr[2], label = "2012")
    plt.plot(month_arr, arr[3], label = "2013")
    plt.plot(month_arr, arr[4], label = "2014")
    plt.plot(month_arr, arr[5], label = "2015")
    plt.legend()
    plt.ylabel("Lượng mưa")
    plt.xlabel("Năm")
    plt.title("Thống kê lượng mưa từng tháng từ năm 2010 - 2015")
    plt.show()
def type_4(df, plt):
    header = data[0]
    data_core = data[1:]
    df = pd.DataFrame(data_core, columns=header)
    year_arr = ["2010", "2011", "2012", "2013", "2014", "2015"]
    month_arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    arr = []
    for i in range(len(year_arr)):
        g = df.groupby("year").get_group(year_arr[i])["temp"].tolist()
        arr_2 = [float(i) for i in g]
        arr.append(arr_2)
    
    plt.plot(month_arr, arr[0], label = "2010")
    plt.plot(month_arr, arr[1], label = "2011")
    plt.plot(month_arr, arr[2], label = "2012")
    plt.plot(month_arr, arr[3], label = "2013")
    plt.plot(month_arr, arr[4], label = "2014")
    plt.plot(month_arr, arr[5], label = "2015")
    plt.legend()
    plt.ylim(15, 30)
    plt.ylabel("Nhiệt độ")
    plt.xlabel("Năm")
    plt.title("Thống kê nhiệt độ từng tháng từ năm 2010 - 2015")
    plt.show()
type_1(df, plt)
type_2(df, plt)
type_3(df, plt)
type_4(df, plt)