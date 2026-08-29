import numpy as np

# 비교 연산 : narray 끼리 각 자리의 요소를 비교 가능
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[1, 0, 3],
                 [4, -2, 9]])

print(arr1 == arr2)
''' 출력 결과 :[[ True False  True]
                [ True False False]]
'''
print(arr1 > arr2)
''' 출력 결과 :[[False  True False]
                [False  True False]]
'''

# array_equal(arr1, arr2) : arr1과 arr2가 같은지 확인하는 함수
print(np.array_equal(arr1, arr2))
# 출력 결과 : False

# 삼각 함수
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
# sin() : 모든 요소에 sin()적용
print(np.sin(arr))
''' 출력 결과 :[[ 0.84147098  0.90929743  0.14112001]
                [-0.7568025  -0.95892427 -0.2794155 ]]
'''
# cos() : 모든 요소에 cos()적용
print(np.cos(arr))
''' 출력 결과 :[[ 0.54030231 -0.41614684 -0.9899925 ]
                [-0.65364362  0.28366219  0.96017029]]
'''
# tan() : 모든 요소에 tan()적용
print(np.tan(arr))
''' 출력 결과 :[[ 1.55740772 -2.18503986 -0.14254654]
                [ 1.15782128 -3.38051501 -0.29100619]]
'''
# pi
print(np.pi)
# 출력 결과 : 3.141592653589793




