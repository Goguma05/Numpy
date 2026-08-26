import numpy as np

# numpy는 리스느 요소의 타입을 보고 적절한 타입을 자동으로 적용시킴
# numpy의 narray는 단일 타입만 허용
arr = np.array([1,2,3])
print(arr, arr.dtype)
# 출력 결과 : [1 2 3] int64

# 요소의 타입을 dtype으로 직접 적용시킬 수 있음
arr = np.array([1, 2, 3], dtype=float)
print(arr, arr.dtype)
# 출력 결과 : [1. 2. 3.] float64
# ㄴ .dtype으로 요소의 타입을 알 수 있음

arr = np.array([1.0, 2.4, 3.8], dtype=int)
print(arr, arr.dtype)
# 출력 결과 : [1 2 3] int64
# ㄴ 실수 타입의 요소를 dtype으로 정수로 적용시키면 소수점 아래를 버림

arr = np.array([0, 1, 1], dtype=bool)
print(arr, arr.dtype)
# 출력 결과 : [False  True  True] bool

arr = np.array([0, 1, 2, 3])
print(arr, arr.dtype)
# 출력 결과 : [0 1 2 3] int64

arr = arr.astype(np.float32)
print(arr, arr.dtype)
# 출력 결과 : [0. 1. 2. 3.] float32
# ㄴ .astype는 narray를 형변환할 수 잇는 함수

arr = np.array([1, 2, 3.4])
print(arr, arr.dtype)
# 출력 결과 : [1.  2.  3.4] float64
# ㄴ float로 통일

arr = np.array([1, 2, 3.4, "64"])
print(arr, arr.dtype)
# 출력 결과 : ['1' '2' '3.4' '64'] <U32
# ㄴ <U32로 통일
''' ㄴ < : 데이터를 낮은 바이트부터 저장
       U : 유니코드 문자열
''' 

arr = np.array([1, 2, 3.4, "64"], dtype=int)
print(arr, arr.dtype)
# 출력 결과 : [ 1  2  3 64] int64
# ㄴ "64"는 유니코드 문자열이 되어서 int로 변경 가능

arr = np.array([1, 2, 3.4, "64", "문자열"], dtype=int)
print(arr, arr.dtype)
# 출력 결과 : ValueError: invalid literal for int() with base 10: '문자열'
# ㄴ 글자는 int로 바꾸기 불가능 -> error