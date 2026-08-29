import numpy as np

# expand_dims() : 새로운 차원을 추가함
arr = np.array([1, 2])
print(arr, arr.shape)
# 출력 결과 :[1 2] (2,)
arr = np.expand_dims(arr, axis=1)
print(arr, arr.shape)
''' 출력 결과 :[[1]
                [2]] (2, 1)
'''

# squeeze() : 차원을 낮춤
arr = np.array([[1, 2]])
print(arr, arr.shape, arr.ndim)
# 출력 결과 : [[1 2]] (1, 2) 2
arr = np.squeeze(arr, axis=0)
print(arr, arr.shape, arr.ndim)
# 출력 결과 : [1 2] (2,) 1

arr = np.array([[1],
                [2],
                [3]])
print(arr, arr.shape, arr.ndim)
''' 출력 결과 :[[1]
                [2]
                [3]] (3, 1) 2
'''
arr = np.squeeze(arr, axis=1)
print(arr, arr.shape, arr.ndim)
# 출력 결과 : [1 2 3] (3,) 1

arr = np.array([[[1, 2, 3]]])
print(arr, arr.shape, arr.ndim)
# 출력 결과 : [[[1 2 3]]] (1, 1, 3) 3
arr = np.squeeze(arr, axis=1)
print(arr, arr.shape, arr.ndim)
# 출력 결과 : [[1 2 3]] (1, 3) 2
# ㄴ axis를 지정하지 않으면 1차원 배열로 축소