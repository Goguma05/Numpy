import numpy as np

# append() : 배열에 마지막 부분에 또 다른 배열을 추가하여 병합
arr1 = np.arange(1, 13).reshape(3, 4)
arr2 = np.arange(13, 25).reshape(3, 4)

print(arr1)
''' 출력 결과 :[[ 1  2  3  4]
                [ 5  6  7  8]
                [ 9 10 11 12]]
'''
print(arr2, end='\n\n')
''' 출력 결과 :[[13 14 15 16]
                [17 18 19 20]
                [21 22 23 24]]
'''

# axis=0
arr3 = np.append(arr1, arr2, axis=0)
print(arr3, end='\n\n')
''' 출력 결과 :[[ 1  2  3  4]
                [ 5  6  7  8]
                [ 9 10 11 12]
                [13 14 15 16]
                [17 18 19 20]
                [21 22 23 24]]
'''

# axis=1
arr3 = np.append(arr1, arr2, axis=1)
print(arr3, end='\n\n')
''' 출력 결과 :[[ 1  2  3  4 13 14 15 16]
                [ 5  6  7  8 17 18 19 20]
                [ 9 10 11 12 21 22 23 24]]
'''
# ㄴ axis를 지정하지 않으면 1차원 배열로 바꿔서 실행


arr1 = np.arange(1, 7).reshape(2, 3)
arr2 = np.arange(7, 13).reshape(2, 3)

# vstack() == append(arr1, arr2, axis=0)
arr3 = np.vstack((arr1, arr2))
print(arr3)
''' 출력 결과 :[[ 1  2  3]
                [ 4  5  6]
                [ 7  8  9]
                [10 11 12]]
'''

# hstack() == append(arr1, arr2, axis=1)
arr3 = np.hstack((arr1, arr2))
print(arr3)
''' 출력 결과 :[[ 1  2  3  7  8  9]
                [ 4  5  6 10 11 12]]
'''


# concatenate()
arr1 = np.arange(1, 7).reshape(2, 3)
arr2 = np.arange(7, 13).reshape(2, 3)

arr3 = np.concatenate([arr1, arr2], axis=0)
print(arr3)
''' 출력 결과 :[[ 1  2  3]
                [ 4  5  6]
                [ 7  8  9]
                [10 11 12]]
'''

''' concatenate와 append 차이점

concatenate
- 튜플, 리스트로 입력을 받음
- axis=9이 기본값
- 기존 축을 기준으로 여러 배열을 연결

append
- 1차원으로 평탕화가 기본값
- 배열의 끝에 요소 또는 배열을 추가
- 반복 사용시 비효율적
'''