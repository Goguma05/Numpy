import numpy as np

# narray 끼리 연산이 가능(일반 연산 기호 사용가능{예시 : +, -, *, /, //, %, **})
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
arr2 = np.array([[2, 2, 2],
                 [2, 2, 2],
                 [2, 2, 2]])
print(arr1)
''' 출력 결과 :[[1 2 3]
                [4 5 6]
                [7 8 9]]
'''
print(arr2)
''' 출력 결과 :[[2 2 2]
                [2 2 2]
                [2 2 2]]
'''

# 덧셈(np.add(arr1, arr2) : narray끼리 같은 자리의 각 요소들 더하기)
print(arr1 + arr2)
print(np.add(arr1, arr2))
''' 출력 결과 :[[ 3  4  5]
                [ 6  7  8]
                [ 9 10 11]]
'''

# 뺄셈(np.subtract(arr1, arr2) : narray끼리 같은 자리의 각 요소들 빼기)
print(arr1 - arr2)
print(np.subtract(arr1, arr2))
''' 출력 결과 :[[-1  0  1]
                [ 2  3  4]
                [ 5  6  7]]
'''

# 곱셈(np.multiply(arr1, arr2) : narray끼리 같은 자리의 각 요소들 곱하기)
print(arr1 * arr2)
print(np.multiply(arr1, arr2))
''' 출력 결과 :[[ 2  4  6]
                [ 8 10 12]
                [14 16 18]]
'''
# ㄴ 내적아님

# 나눗셈(np.divide(arr1, arr2) : narray끼리 같은 자리의 각 요소들 나누기)
print(arr1 / arr2)
print(np.divide(arr1, arr2))
''' 출력 결과 :[[0.5 1.  1.5]
                [2.  2.5 3. ]
                [3.5 4.  4.5]]
'''

# 제곱(np.square(arr1, arr2) : narray끼리 같은 자리의 각 요소들 제곱하기)
print(arr1 ** 5)
''' 출력 결과 :[[    1    32   243]
                [ 1024  3125  7776]
                [16807 32768 59049]]
'''
print(np.square(arr1))
''' 출력 결과 :[[ 1  4  9]
                [16 25 36]
                [49 64 81]]
'''

# 제곱근(np.sqrt(arr1, arr2) : narray끼리 같은 자리의 각 요소들 제곱근하기)
print(np.sqrt(arr1))
''' 출력 결과 :[[1.         1.41421356 1.73205081]
                [2.         2.23606798 2.44948974]
                [2.64575131 2.82842712 3.        ]]
'''

# 몫
print(arr1 // 2)
''' 출력 결과 :[[0 1 1]
                [2 2 3]
                [3 4 4]]
'''

# 나머지
print(arr1 % 2)
''' 출력 결과 :[[1 0 1]
                [0 1 0]
                [1 0 1]]
'''