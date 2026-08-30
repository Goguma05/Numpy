import numpy as np

# 실습 예제 1
# 원소가 모두 3인 (3,4,5) 형태의 numpy.array를 출력하시오.

# 답안 작성
arr = np.full((3, 4, 5), 3)
print(arr)

# 풀이
arr = np.full((3, 4, 5), 3)
print(arr)

# 실습 예제 2
''' 정수 -50 ~ 50의 범위 안의 난수로 이루어진 (4,5) 형태의 numpy.array를
    출력하고 행을 기준으로 오름차순 정렬한 결과와 전체 배열을 1차원 배열로
    변경하여 오름차순 정렬한 결과를 출력하시오
'''

# 답안 작성
arr = np.random.randint(-50, 50, size=(4,5))
arr_sorted = np.sort(arr, axis=0)
arr_sorted1 = np.sort(arr, axis=None)
print(arr)
print(arr_sorted)
print(arr_sorted1)

# 풀이
arr = np.random.randint(-50, 50, (4,5))
print(arr)
print(np.sort(arr, axis=0))
print(np.sort(arr, axis=None))

# 실습 예제 3
''' 다음과 같은 파이썬 list가 존재한다.
    list 안에 있는 각 numpy.array의 원소들의 평균값과 표준편차, 중앙값을
    순서대로 구하여 구한 순서대로 원소가 이루어진 새로운 list를
    구성하고 출력하시오.
'''
py_list = [
    np.full(3, 8),
    np.array([33, -15, 26]),
    np.linspace(17, 26, 3)
]

# 답안 작성
answer = []
for lst in py_list:
    answer.append(np.mean(lst))
    answer.append(np.std(lst))
    answer.append(np.median(lst))
print(answer)

# 풀이
result_arr = []
for i in py_list:
    result_arr.append(np.mean(i))
    result_arr.append(np.std(i))
    result_arr.append(np.median(i))
print(result_arr)
