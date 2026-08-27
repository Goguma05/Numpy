import numpy as np

# Boolean 인덱싱
arr = np.array([1, 2, 3, 4])
print(arr[[True, False, True, True]])
# 출력 결과 : [1 3 4]

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])
print(arr[[True, False], True])
# 출력 결과 : [[1 2 3 4]]

# 조건문으로 값을 가져올 수 있음
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])
print(arr[arr > 3])
# 출력 결과 : [4 5 6 7 8]
print(arr[arr <= 2])
# 출력 결과 : [1 2]


