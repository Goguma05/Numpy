import numpy as np

# 브로드캐스팅 : 두 행렬이 연산이 되게 하기 위해 같은 크기로 바꿔 연산하게 하는 기법
arr1 = np.array([[0, 0, 0],
                 [1, 1, 1],
                 [2, 2, 2]])
arr2 = np.array([5, 6, 7])
print(arr1 + arr2)
''' 출력 결과 :[[5 6 7]
                [6 7 8]
                [7 8 9]]
'''

arr1 = np.array([1, 1, 1])
arr2 = np.array([[0],
                [1],
                [2]])
print(arr1 + arr2)
''' 출력 결과 :[[1 1 1]
                [2 2 2]
                [3 3 3]]
'''


