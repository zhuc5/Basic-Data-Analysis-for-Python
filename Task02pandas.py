# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
# =============================================================================
# 第五章panda入门
# =============================================================================
# =============================================================================
# =============================================================================
# 一.pandas 数据结构
# type 1: series
# 一种一维数组，由value和index构成；
# 
# * 创建方式：
# obj = pd.Series([4,5,6,7])
# obj = pd.Series([4,5,6,7], index = ['a','b','c','d']) #创建索引
# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000,'Utah': 5000}
# obj3 = pd.Series(sdata) # 通过字典创建；该种方法可以传入定义好的index
# states = ['California', 'Ohio', 'Oregon', 'Texas']
# obj4 = pd.Series(sdata, index=states)
# 
# * 引用：
# 通过索引的方式选取 Series 中的单个或一组值；也可以选中某个index赋值更改原数组；
# obj['d'],obj[['a','b']]
# obj[obj>6] 
# np.exp(obj)
# 注：使用 NumPy 函数或类似 NumPy 的运算(如根据布尔型数组进行过滤、标量乘 法、应用数学函数等)都会保留索引值的链接
# 
# * 使用方式：
# 1.1 将Series 看成是一个定长的有序字典
# 'b' in obj
# 1.2 isnull 和 notnull 函数可用于检测缺失数据
# pd.isnull(obj4)
# obj4.isnull()
# 1.3 **** Series 最重要的一个功能是根据运算的索引标签自动对齐数据 ***
# obj3 + obj4 # 类似于join
# 1.4 Series 对象本身及其索引的 name 属性
# obj4.name = 'population'
# obj4.index.name = 'state'
# 
# 
# type 2: DataFrame
# 一个表格型的数据结构；每列类型可以不同；DataFrame 既有行索引也有列索引
# 
# * 创建方式：
# a.传入一个由等长列表或 NumPy 数组组成的字典
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada',
# 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002, 2003],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# frame = pd.DataFrame(data)
# 
# * 使用方式
# 1.1frame.head()
# 1.2 若指定列序列，则 DataFrame 的列就会按照指定顺序进行排列；
# frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop','debt'],index=['one', 'two', 'three', 'four','five', 'six'])
# ps:如果传入的列在数据中找不到，就会在结果中产生缺失值；
# 1.3 通过类似字典标记的方式或属性的方式，可以将 DataFrame 的列获取为一个 Series
# frame2['state']
# frame2.year
# ps：frame2[column]适用于任何列的名，但是 frame2.column 只有在列名是一个合理的 Python 变量名时才适用
# 1.4 通过位置或名称的方式获取行信息
# frame2.loc['three']
# 1.5 列可以通过赋值的方式进行修改
# frame2['debt'] = 16.5 # 赋一个值
# frame2['debt'] = np.arange(6.) # 赋一组值
# ps:将列表或数组赋值给某个列时，其长度必须跟 DataFrame 的长度相匹配
# 赋值的是一个 Series，就会精确匹配 DataFrame 的索引，所有的空位都将补上缺失值,且为不存在的列赋值会创建出一个新列
# val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four','five'])
# frame2['debt'] = val
# 1.6 del 用于删除列
# del frame2['eastern']
# 1.7 若嵌套字典传给 DataFrame，pandas 就会被解释为:外层字典的键作为列，内层键则作为行索引
# pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
# frame3 = pd.DataFrame(pop)
# 1.8 对 DataFrame 进行转置
# frame3.T
# 1.9 视图--通过索引方式返回的列：对返回的 Series 所做的任何就地修改全都会反映到源 DataFrame
# 副本--Series 的 copy 方法：不会改变源数据
# 1.10 DataFrame的index和columns的name属性
# frame3.index.name = 'year'
# frame3.columns.name = 'state'
# 1.11 取数 frame3.values
# 
# * 索引对象
# 1.1 index对象：
# obj = pd.Series(range(3), index=['a', 'b', 'c'])
# index = obj.index
# ps：index对象不可更改，可以像列表一样被切片索引
# 不可变可以使 Index 对象在多个数据结构之间安全共享
# labels = pd.Index(np.arange(3))
# obj2 = pd.Series([1.5, -2.5, 0], index=labels)
# 可以用in检测元素
# 'Ohio' in frame3.columns
# pandas 的 Index 可以包含重复的标签
# pd.Index(['foo', 'foo', 'bar', 'bar'])
# 
# 二.pandas常用功能探索
# 1.重新索引 reindex
# 创建一个新对象，它的数据符合新的索引
# obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
# 1.2 method方法 前向值填充
# obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# obj3.reindex(range(6), method='ffill')
# obj3
# 
# 2.丢弃指定轴上的项 -- drop 方法
# * series类型
# obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
# new_obj = obj.drop('c')
# obj.drop(['d', 'c'])
# 
# * dataframe 类型
# data.drop(['Colorado', 'Ohio']) # 默认 drop 从行标签(axis 0)删除值
# data.drop('two', axis=1) # 也可通过传递 axis=1 或 axis='columns'可以删除列的值
# data.drop(['two', 'four'], axis='columns')
# # =============================================================================
# # 设置inplace可以就地修改对象，不会返回新的对象
# # ps：利用标签的切片运算与普通的 Python 切片运算不同，其末端是包含的
# # =============================================================================
# =============================================================================
