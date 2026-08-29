import numpy as np

# 전치행렬 : y = -x 그래프 대칭
arr = np.array([[1, 2],
                [3, 4]])
print(arr.T)
''' 출력 결과 :[[1 3]
                [2 4]]
'''

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr.T)
''' 출력 결과 :[[1 4 7]
                [2 5 8]
                [3 6 9]]
'''

arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])
print(arr.T)
''' 출력 결과 :[[1 3 5]
                [2 4 6]]
'''