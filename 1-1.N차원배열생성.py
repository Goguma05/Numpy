import numpy as np

# 1차원 배열
arr = np.array([1,2,3])
print(arr) 
# 출력 결과 : [1 2 3]

# 2차원 배열
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr) 
''' 
출력 결과 : [[1 2 3]
             [4 5 6]]
'''

print(type([1, 2, 3]))
print(type(arr))
print("np.array != list -> ", type(arr) == type([1, 2, 3]))
'''
출력 결과 : <class 'list'>
            <class 'numpy.ndarray'>
            np.array != list ->  False
'''
# ㄴ 리스트와 넘파이array는 다른 타입

tpl = (4, 5, 6)
arr = np.array(tpl)
print(arr)

lst = [1, 2, 3]
arr = np.array(lst)
print(arr)

lst2 = [[1, 2, 3], [4, 5, 6]]
arr2 = np.array(lst2)
print(arr2)
'''
출력 결과 : [4 5 6]
            [1 2 3]
            [[1 2 3]
            [4 5 6]]
'''

# shape (narray의 크기)
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])

print(arr1.shape, arr2.shape)
# 출력 결과 : (3,) (2, 3)

# ndim (narray의 차원)
print(arr1.ndim, arr2.ndim)
# 출력 결과 : 1 2

# size (narray의 요소 개수)
print(arr1.size, arr2.size)
# 출력 결과 : 3 6

