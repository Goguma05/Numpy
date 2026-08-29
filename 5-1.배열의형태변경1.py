import numpy as np

arr = np.arange(12)
print(arr, arr.ndim)
# 출력 결과 : [ 0  1  2  3  4  5  6  7  8  9 10 11] 1

# reshape(size) : narray의 형태를 변경
arr = arr.reshape((3, 4))
print(arr, arr.ndim)
''' 출력 결과 :[[ 0  1  2  3]
                [ 4  5  6  7]
                [ 8  9 10 11]] 2
'''
# ㄴ narray의 요소 개수에 맞게 형태를 변경해야함

arr = arr.reshape((2, 3, 2))
print(arr, arr.ndim)
''' 출력 결과 :[[[ 0  1]
                [ 2  3]
                [ 4  5]]

                [[ 6  7]
                [ 8  9]
                [10 11]]] 3
'''

arr = arr.reshape((2, 2, 1, 3))
print(arr, arr.ndim)
''' 출력 결과 :[[[[ 0  1  2]]
                [[ 3  4  5]]]
                [[[ 6  7  8]]
                [[ 9 10 11]]]] 4
'''

# 차원의 저주 : 차원이 늘어날 수록 데이터들 사이의 간격이 넓어짐