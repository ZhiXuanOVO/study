from pandas import Series,DataFrame
import pandas as pd
import numpy as np
data = {
    '张三':88,
    '李四':76,
    '王五':92,
    '赵六':65
}
s1 = Series(data)
print(s1)
print(s1.index)
print(s1.values)
print(s1['王五'])
print(s1['李四':'赵六'])
s1['赵六'] = 78
print(s1)