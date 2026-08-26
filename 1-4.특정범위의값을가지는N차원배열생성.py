import numpy as np

# np.arange() : range()의 numpy 버전
arr = np.arange(9)
print(arr)
# 출력 결과 : [0 1 2 3 4 5 6 7 8]
arr = np.arange(3, 13)
print(arr)
# 출력 결과 : [ 3  4  5  6  7  8  9 10 11 12]
arr = np.arange(3, 13, 3)
print(arr)
# 출력 결과 : [ 3  6  9 12]

# np.linspace() : start부터 stop까지 step개의 균등한 간격으로 생성
arr = np.linspace(0, 100, 11)
print(arr)
# 출력 결과 : [  0.  10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]

# np.logspace() : 로그 단위로 linspace()
arr = np.linspace(1, 10, 10)
print(arr, end='\n\n')
# 출력 결과 : [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

arr = np.logspace(1, 10, 10, base=2)
print(arr)
# 출력 결과 : [   2.    4.    8.   16.   32.   64.  128.  256.  512. 1024.]

arr = np.logspace(1, 10, 10)
print(arr)
# 출력 결과 : [1.e+01 1.e+02 1.e+03 1.e+04 1.e+05 1.e+06 1.e+07 1.e+08 1.e+09 1.e+10]
# ㄴ base 기본값 10(상용로그)