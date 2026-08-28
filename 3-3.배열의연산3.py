import numpy as np

arr = np.array([[1, 2, 3],
                [0, 1, 4]])
# axis : 0은 행, 1은 열
# min() : 최솟값
print(np.min(arr))
print(arr.min())
# 출력 결과 : 0
print(arr.min(axis=1))
# 출력 결과 : [1, 0]

# max() : 최댓값
print(np.max(arr))
print(arr.max())
# 출력 결과 : 4
print(arr.max(axis=0))
# 출력 결과 : [1, 2, 4]

# sum() : 합
print(np.sum(arr))
print(arr.sum())
# 출력 결과 : 19
print(arr.sum(axis=0))
# 출력 결과 : [2 8 9]

# mean() : 평균
print(np.mean(arr))
print(arr.mean())
# 출력 결과 : 2.111111111111111
print(arr.mean(axis=1))
# 출력 결과 : [2.         1.66666667 2.66666667]

# std() : 표준편차
print(np.std(arr))
print(arr.std())
# 출력 결과 : 1.5234788000891208
print(arr.std(axis=0))
# 출력 결과 : [0.47140452 1.69967317 0.81649658]

# cumsum() : 누적합계
print(np.cumsum(arr))
print(arr.cumsum())
# 출력 결과 : [ 1  3  6  6  7 11 12 17 19]
print(arr.cumsum(axis=1))
''' 출력 결과 :[[1 3 6]
                [0 1 5]
                [1 6 8]]
'''

arr = np.array([[1, 2, 3],
                [0, 1, 4],
                [1, 5, 2]])

# median() : 중앙값
print(np.median(arr, axis=1))
# 출력 결과 : [2. 1. 2.]