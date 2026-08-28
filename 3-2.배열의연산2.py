import numpy as np

# 1차원 배열
# 1차원 내적 : 같은 자리 요소끼리 곱하고 나온 결과값들을 다 합함
arr1 = np.array([2, 3, 4])
arr2 = np.array([1, 2, 3])

print(np.dot(arr1, arr2))
# 출력 결과 : 20

# 2차원 배열
'''2차원 내적 : A(1행) B(1열) 1차 내적, A(1행) B(2열) 1차 내적, 
                A(2행) B(1열) 1차 내적, A(2행) B(2열) 1차 내적
                1차 내적의 연속

[[a, b], [[e, f],    [[ae+bg, af+ah],
 [c, d]]  [g, h]] =>  {ce+dg, cf+dh}]
'''

arr1 = np.array([[1, 2],
                 [4, 5]])
arr2 = np.array([[1, 2],
                 [0, 3]])
print(np.dot(arr1, arr2))
''' 출력 결과 :[[ 1  8]
                [ 4 23]]
'''

# 절댓값
arr1 = np.array([[1, -2],
                 [-4, 5]])
print(np.abs(arr1))
''' 출력 결과 :[[1 2]
                [4 5]]
'''

# 올림
arr1 = np.array([[1.932, -2.339],
                 [-4.145, 5.206]])
print(np.ceil(arr1))
''' 출력 결과 :[[ 2. -2.]
                [-4.  6.]]
'''

# 내림
print(np.floor(arr1))
''' 출력 결과 :[[ 1. -3.]
                [-5.  5.]]
'''

# 반올림
print(np.round(arr1))
''' 출력 결과 :[[ 2. -2.]
                [-4.  5.]]
'''

# 버림
print(np.trunc(arr1))
''' 출력 결과 :[[ 1. -2.]
                [-4.  5.]]
'''
