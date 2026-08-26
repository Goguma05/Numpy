import numpy as np

# np.zeros() : 주어진 크기로 모든 요소에 0을 채워서 생성
arr = np.zeros([2, 2])
print(arr)
''' 출력 결과 : [[0. 0.]
                [0. 0.]]
'''

# np.ones() : 주어진 크기로 모든 요소에 1을 채워서 생성
arr = np.ones([2, 3])
print(arr)
''' 출력 결과 : [[1. 1. 1.]
                [1. 1. 1.]]
'''

# np.full() : 주어진 크기로 모든 요소에 지정한 n을 채워서 생성
arr = np.full((2, 3), 5)
print(arr)
''' 출력 결과 : [[5 5 5]
                [5 5 5]]
'''

# np.eye() : 대각 요소가 1인 행렬 생성
arr = np.eye(3, 4, k=0)
print(arr)
''' 출력 결과 : [[1. 0. 0. 0.]
                [0. 1. 0. 0.]
                [0. 0. 1. 0.]]
'''
# ㄴ n만 주어지면 nxn 정방행렬 생성
#    k의 기본 값은 0

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# np.zeros_like() : 주어진 행렬의 요소들을 0으로 채움
arr_z = np.zeros_like(arr)
print(arr_z)
''' 출력 결과 : [[0 0 0]
                [0 0 0]]
'''

# np.ones_like() : 주어진 행렬의 요소들을 1로 채움
arr_o = np.ones_like(arr)
print(arr_o)
''' 출력 결과 :[[1 1 1]
                [1 1 1]]
'''

# np.full_like() : 주어진 행렬의 요소들을 지정한 n으로 채움
arr_f = np.full_like(arr, 9)
print(arr_f)
''' 출력 결과 : [[9 9 9]
                [9 9 9]]
'''