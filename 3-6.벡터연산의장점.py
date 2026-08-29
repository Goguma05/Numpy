import numpy as np
import time

# 벡터 연산의 장점 : 일반 for문으로 연산할 때와 벡터 연산할 때 걸리는 시간차이가 크다.
arr = np.arange(99999999)

# for
sum = 0
before = time.time()
for i in arr:
    sum += i
after = time.time()
print(sum, after - before, "초")
# 출력 결과 : 4999999850000001 28.155027151107788 초

# 벡터 연산
before = time.time()
sum = np.sum(arr)
after = time.time()
print(sum, after - before, "초")
# 출력 결과 : 4999999850000001 0.08233880996704102 초

arr1 = np.arange(99999999)
arr2 = np.arange(99999999)

# for
sum = 0
before = time.time()
for i, j in zip(arr1, arr2):
    sum += i * j
after = time.time()
print(sum, after - before, "초")
# 출력 결과 : 652921401952298879 40.49971556663513 초

# 벡터 연산
before = time.time()
sum = np.dot(arr1, arr2)
after = time.time()
print(sum, after - before, "초")
# 출력 결과 : 652921401952298879 0.1680011749267578 초