import numpy as np

arr = np.random.rand(10)
print("난수 발생1 \n", arr)

arr = np.random.rand(10)
print("난수 발생2 \n", arr)

np.random.seed(1)
arr = np.random.rand(10)
print("난수 발생1 \n", arr)

np.random.seed(1)
arr = np.random.rand(10)
print("난수 발생2 \n", arr)
# ㄴ 시드가 같은 난수는 동일한 결과를 얻음
# ㄴ 난수는 첫 시드에서 특정 계산식을 이용해 얻는 방식ㅉ