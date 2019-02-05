from pandas import Series, DataFrame
import pandas as pd

# # 索引
# #一维数组
# # obj = Series([4,5,-7])
# # print(obj)
# #
# # print(obj.values)
# # print(obj.index)
# #
# # p = {'a':1,'b':2, 'c': 3}
#
#
# obj2 = Series([4,5,-7,5],index = ['a','b','c','d'])
#
# print(obj2)
#
# data = {'city': ['zhengzhou','shanghai','guangzhou','beijing'],
#         'year': [2008,1989,2019,2005],
#         'pop': [1.4,8.3,7.6,10.5]}
#
# frame = DataFrame(data)
# print(frame)
#
# # 排序
#
# frame2 = DataFrame(data,columns=['year','pop','city'])
# print(frame2)
#
# print(frame2['city'])
#
# # 增加新列
# frame2['new'] = 100
# print(frame2)
#
# # 条件判断
# frame2['cap'] = frame2.city =='beijing'
# print(frame2)
#
# # 互换
# pop = {'beijing':{2008:1.5,2018:10.5},
#        'shanghai':{2008:7.5,2018:15.5}
#     }
# frame3 = DataFrame(pop)
# print(frame3)
# print(frame3.T)

# obj4 = Series([4.5,7.2,-5.3,3.6], index=['b','d','c','g'])
# obj5 = obj4.reindex(['a','b','c','d','e'],fill_value=0)
#
# print(obj5)

# obj6 = Series(['blue','yellow','purple'], index= [0,2,4])
# print(obj6.reindex(range(6),method='bfill'))

# 删除

from numpy import nan as NA

# data = Series([1,NA,2])
# print(data)
# print(data.dropna())

data1 = DataFrame([[1,2,NA],[NA,NA,NA],[1,88,5]])
print(data1)
print(data1.dropna(axis=1, how='all'))
# data1.fillna(0)
# print(data1)
