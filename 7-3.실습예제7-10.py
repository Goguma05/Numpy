import numpy as np

# 실습 예제 7
''' 다음 두 행렬에 대하여 내적 연산을 수행한 결괏값을 출력하시오.
    (단, 결과의 소수점 아래는 제거한다.)
'''
A = np.array([[2.1, 3.5],
              [4.2, 2.7],
              [2.3, 1.9]])
B = np.array([[5, 2, 3],
              [1, 3, 5]])

# 답안 작성
answer = np.dot(A, B)
print(np.trunc(answer))

# 풀이
print(np.trunc(np.dot(A, B)))

# 실습 예제 8
''' 조건 연산자를 활용한 Boolean 인덱싱을 이용하여 다음 배열의 원소들 중
    2와 5의 배수만 추출한 결과를 오름차순 정렬하여 (2, 4) 행렬로 출력하시오.
'''
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
# 답안 작성
'''arr_bool = arr[arr % 2 == 0]

print(arr_bool)
arr1 = np.sort(arr_bool, axis=None)
print(arr1.reshape((2,4)))
'''
# 풀이
print(np.sort(np.append(arr[arr % 2 == 0], arr[arr % 5 == 0])).reshape((2, 4)))

# 실습 예제 9
''' 10진수 100이상 150미만 사이에 존재하는 정수를 무작위로 추출하여
    (3, 10) 형태의 행렬로 만들고 행과 열을 전치한 결과를 출력하시오.
'''
# 답안 작성
arr = np.random.randint(100, 150, (3, 10))
print(arr)
print(arr.T)
# 풀이

# 실습 예제 10
''' 10진수 10~20 사이에 존재하는 실수형의 수룰 뮤작위로 10000개 추출하여
    100개의 구간에 그래프로 시각화하시오.
    (단, 무작위 실수 값은 균등한 비율로 추출해야 하며
    그래프 시각화 도구는 pyplot 모듈을 사용할 것)
'''
import matplotlib.pyplot as plt
# 답안 작성
'''x = np.random.randint(10, 20, 10000)
plt.hist(x, bins=100)
plt.show()'''

# 풀이
arr = 10 + np.random.rand(10000) * 10
plt.hist(arr, bins=100)
plt.show()