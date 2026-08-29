import numpy as np

# 1차원 배열의 정렬
arr = np.random.randint(10, size=10)
print(arr)
# 출력 결과 : [1 0 6 3 4 3 0 4 8 9]

# sort(arr) : arr의 요소들을 오름차순으로 정렬
print(np.sort(arr))
# 출력 결과 : [0 0 1 3 3 4 4 6 8 9]
# ㄴ 정렬된 배열을 반환함
print(np.sort(arr)[::-1])
# 출력 결과 : [9 8 6 4 4 3 3 1 0 0]
# ㄴ 오름차순으로 정렬된 배열을 뒤집어 출력

# sort()는 원본 배열에 영향 끼치지 않음
arr = np.sort(arr)
print(arr)
# 출력 결과 : [0 0 1 3 3 4 4 6 8 9]