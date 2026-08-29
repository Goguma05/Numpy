import numpy as np

# 2차원 배열의 정렬
arr = np.random.randint(15, size=(3,4))
print(arr)
''' 출력 결과 :[[ 7  0 13  2]
                [ 6  5  0  7]
                [ 7  7  1  9]]
'''

# ㄴ sort()는 axis=1이 기본값
print(np.sort(arr, axis=0))
''' 출력 결과 :[[ 6  0  0  2]
                [ 7  5  1  7]
                [ 7  7 13  9]]
'''
print(np.sort(arr, axis=None))
# 출력 결과 : [ 0  0  1  2  5  6  7  7  7  7  9 13]
# ㄴ axis=None이면 1차원 배열로 바꿔서 정렬

# argsort(arr) : 정렬되기 전 인덱스를 표기
print(np.sort(arr, axis=1))
''' 출력 결과 :[[ 0  2  7 13]
                [ 0  5  6  7]
                [ 1  7  7  9]]
'''
print(np.argsort(arr, axis=1))
''' 출력 결과 :[[1 3 0 2]
                [2 1 0 3]
                [2 0 1 3]]
'''