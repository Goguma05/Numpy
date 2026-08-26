import numpy as np
import matplotlib.pyplot as plt

# np.random.normal(loc, scale, size) : loc(정규분포의 평균)와 scale(표준편차)인 정규 분포에서 size(추출할 표본 개수)크기의 narray 생성
arr = np.random.normal(0, 1, 10)
print(arr)
# 출력 결과 : [ 0.58354111  0.41367059 -0.42437761  1.30365427 -0.95682243  0.58675842 0.88496523 -0.37856454  0.83177847  0.66264395]

arr = np.random.normal(0, 1, (2, 3))
print(arr)
''' 출력 결과 : [[-1.23098257 -0.44444148  2.61976436]
                [-1.8086593   1.02399705 -0.46946438]]
'''

arr = np.random.normal(0, 1, 1000)
print(arr)
plt.hist(arr ,bins=100)
plt.show()

# np.random.rand(n) : 0에서 1사이에 정규분포에서 값을 균등하게 추출
arr = np.random.rand(100)
print(arr)
plt.hist(arr, bins=100)
plt.show()

# np.random.randn(n) : -1에서 1사이에 정규분포에서 값을 균등하게 추출
arr = np.random.randn(100)
print(arr)
plt.hist(arr, bins=100)
plt.show()

# np.random.randint(low, high, size) : : 지정한 low에서 high 미만까지 size 크기의 랜덤한 요소를 가진 행렬 생성
arr = np.random.randint(1, 5, 10)
print(arr)
# 출력 결과 : [2 3 4 3 1 3 1 2 3 2]
