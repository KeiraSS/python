import numpy as np

# arr1 = np.array([2,3,4])
# print(arr1)
# print(arr1.dtype)
#
# arr2 = np.array([1.1,2.3,44.3])
# print(arr2)
# print(arr2.dtype)
#
# # 列表累加
# print(arr1+arr2)
#
# print(arr2 *2)
#
# 矩阵
# data = [[1,2,3],[4,5,6]]
# arr3 = np.array(data)
# print(arr3)
# print(arr3.dtype)
#
# print(np.zeros((3,5)))
# print(np.ones((2,7)))
#
# # 填充随机值
# print(np.empty((2,3,2)))


arr4 = np.arange(10)
arr4[5:8] = 10  # 5和8改成10
print(arr4)

arr_slice = arr4[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr4)