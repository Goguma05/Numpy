import numpy as np

# python list
arr = [1, 2, 3, 4, 5, 6, 7, 8]
arr.insert(2, 50)
print(arr)
# 출력 결과 : [1, 2, 50, 3, 4, 5, 6, 7, 8]

# insert(arr, index, value) : arr의 index번호 쪽에 value를 삽입

# 1차원 배열
arr = np.arange(1, 9)
arr = np.insert(arr, 2, 50)
print(arr)
# 출력 결과 : [ 1  2 50  3  4  5  6  7  8]

# 2차원 배열
arr = np.arange(1, 13).reshape(3, 4)
arr = np.insert(arr, 2, 50, axis=1)
print(arr)
''' 출력 결과 :[[ 1  2 50  3  4]
                [ 5  6 50  7  8]
                [ 9 10 50 11 12]]
'''

# delete(arr, index) : arr의 index번호 쪽을 삭제
arr = np.arange(1, 13).reshape(3, 4)
print(arr)
''' 출력 결과 :[[ 1  2  3  4]
                [ 5  6  7  8]
                [ 9 10 11 12]]
'''
arr = np.delete(arr, 2, axis=1)
print(arr)
''' 출력 결과 :[[ 1  2  4]
                [ 5  6  8]
                [ 9 10 12]]
'''

# ㄴ axis를 지정하지 않으면 1차원 배열로 바꾸고 실행