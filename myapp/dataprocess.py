import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileNameStr = './20200621192345136_1731.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8')
#df.head(10)
#DataDF.head().to_string()
#使用to_string()方法，out就不是表格，基本就是无法看的数据，还是去到原始csv文件里，删掉一些空值很多的列
print(df.index)#看一下index的索引信息，
print("===========")
print(df.columns)#看一下columns的索引信息
print("-----------")
print(type(df.index))
print(type(df.columns))
#index和columns都是索引类型，不是常规的series或者是dataframe类型

#删除不需要的属性列
drop_name_time = ["车辆Vin","时间"]
keep_columns = []
df.drop(columns=drop_name_time,axis=1,inplace= True)
#方才想要删除drop_name_time的时候试了很多次，可能有一个已经删掉了，
#或者是已经删除了，你还删除，那肯定没有，应该有个参数，没有的列删除不报错就好了，可能这里有个异常抛出一下比较好，有时间再看看
#df.head(3)
#这里试一下describe()和循环打印columns的索引和值,describe函数只统计了数字类型的column
df_describe = df.describe()
df_describe_T = df_describe.T
#df_describe_T

#统计每一列属性的非空值占比
maxrows = df.index.size
df_describe_T['expectedcount'] = maxrows
df_describe_T['nancount']= maxrows -df_describe_T['count']
#df_describe_T

#统计异常值占比，没写完
Q1 = df_describe_T['25%']
Q3 = df_describe_T['75%']
IQR = Q3 - Q1
low = Q1 - 1.5*IQR
high = Q3 + 1.5*IQR
df_describe_T['limitlow'] = low
df_describe_T['limithigh'] = high
df_describe_T['outliercount'] = np.nan
#df_describe_T
df_describe = df_describe_T.T





#df_describe

#统计所有csv文件 x：累计充电，y：有效记录个数，柱状图
