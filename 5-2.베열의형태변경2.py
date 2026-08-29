import numpy as np

arr = np.arange(12)
print(arr)
# 출력 결과 : [ 0  1  2  3  4  5  6  7  8  9 10 11]
# resize() : 원본 narray의 형태 변경(reshape은 복사한 narray의 형태 변경 후 반환)
arr.resize(3, 4)
print(arr)
''' 출력 결과 :[[ 0  1  2  3]
                [ 4  5  6  7]
                [ 8  9 10 11]]
'''
# ㄴ 원본 배열의 개수에 맞게 크기를 조절할 필요없음

# ravel() 1차원 배열로 변경
arr = arr.ravel()
print(arr)
# 출력 결과 : [ 0  1  2  3  4  5  6  7  8  9 10 11]

arr = np.arange(1, 13)
print(arr)
# 출력 결과 : [ 1  2  3  4  5  6  7  8  9 10 11 12]

# -1은 크기를 자동으로 계산(요소의 개수가 12니까 3이면 4로)
arr = arr.reshape(3, -1)
print(arr)
''' 출력 결과 :[[ 1  2  3  4]
                [ 5  6  7  8]
                [ 9 10 11 12]]
'''

arr = arr.reshape(3, 2, -1)
print(arr)
''' 출력 결과 :[[[ 1  2]
                [ 3  4]]

                [[ 5  6]
                [ 7  8]]

                [[ 9 10]
                [11 12]]]
'''

arr = arr.reshape(3, -1, -1)
print(arr)
''' 출력 결과 : ValueError: can only specify one unknown dimension
지정되지 않은 차원은 2개 이상이면 안된다.
'''
# ㄴ 지정되지 않은게 1개여야함(-1이 2개 이상이면 안됨)


