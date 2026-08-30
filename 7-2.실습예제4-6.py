import numpy as np

# 실습 예제 4
''' 다음과 같은 numpy.array가 존재한다. 이 배열을 행을 기준으로 3개의 배열로
    분할하여 분할된 각 배열의 원소들을 제곱한 결과를 다시 원본 배열에 행을
    기준으로 병합하시오.
    (단, 마지막 출력 결과는 원본 배열과 차원이 같아야 한다)
'''
arr = np.arange(2, 20, 2).reshape((3, 3))
# 답안 작성
arr_vsplit = np.vsplit(arr, 3)
for i in arr_vsplit:
    arr = np.concatenate([arr, i**2], axis=0)
print(arr)

#풀이
arr = np.arange(2, 20, 2).reshape((3, 3))
s1 = np.vsplit(arr, 3)
print(s1)
s2 = np.square(s1)
print(s2)
s3 = np.squeeze(s2, axis=1)
print(s3)
result_arr = np.vstack((arr, s3))
print(result_arr)

# 실습 예제 5
''' 삼각함수의 특수각(0, 30, 60, 90)을 numpy.array로 생성한 후
    특수각에 해당하는 sin,cos,tan 값을 각가 구하여
    파이썬 list에 담은 다음 해당 list에 들어잇는 값들을 출력하시오.
    (단, 값이 무한대라면 "INF" 문자열을 출력할 것)
'''
# 답안 작성
degree = np.array((0, 30, 60, 90))
s = np.sin(degree*np.pi / 180)
c = np.cos(degree*np.pi / 180)
t = np.tan(degree*np.pi / 180)
answer = [s, c, t]
print(answer[0])
print(answer[1])
print(answer[2])

#풀이
arr = np.arange(0, 91, 30)
print(arr)
lst = []
lst.append(np.sin(arr * np.pi / 180))
lst.append(np.cos(arr * np.pi / 180))
lst.append(np.tan(arr * np.pi / 180))

for value_lst in lst:
    for value in value_lst:
        if value > 999999999:
            print("INF")
            continue
        print(value)
    print()
# 실습 예제 6
''' numpy.array를 이용하여 다음과 같은 패턴을 출력하시오
    (단, 출력 시 반복문을 사용하여 출력 한다.)
'''
# 답안 작성
arr = np.arange(0, 49)
arr_bool = arr[arr % 2].reshape((7, 7))
for value_lst in arr[arr_bool]:
    for value in value_lst:
        print(value, end=' ')
    print()


#풀이
arr = np.zeros((7, 7), dtype=int)

arr[::2, 1::2] = 1
arr[1::2, ::2] = 1

for row in range(7):
    for col in range(7):
        print(arr[row,col], end=' ')
    print()