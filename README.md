# Numpy

Numpy의 기초와 사용방법을 공부하기 위한 프로젝트입니다.

__함수__

**numpy.array(object, dtype)** : 예시) numpy.array([1,2,3], dtype = float)

매개변수
- **object** : NumPy 배열로 변환할 데이터(파이썬 리스트, 튜플 등)입니다.
- **dtype** : 원소들의 타입을 정할 수 있습니다.

속성
- **.shape** : 배열의 차원별 크기를 튜플형태로 반환합니다.
- **.ndim** : 배열의 차원(축)의 수를 반환합니다.
- **.size** : 배열의 전체 원소의 개수를 반환합니다.
- **.dtype** : 원소의 현재 타입을 반환합니다.

특징
- 배열을 생성하고 반환합니다.
- 타입은 "numpy.ndarray"입니다.
- 배열의 원소들은 같은 타입으로 통일 시킵니다.

**numpy.zeros(shape)** : 예시) numpy.zeros([2, 2])

매개변수
- **shape** : 생성할 배열의 크기나 구조를 지정합니다.

특징
- 주어진 크기만큼 모든 원소의 값을 0으로 채워 생성하고 반환합니다.

**numpy.ones(shape)** : 예시) numpy.ones([2,3])

매개변수
- **shape** : 생성할 배열의 크기나 구조를 지정합니다.

특징
- 주어진 크기만큼 모든 원소의 값을 1로 채워 생성하고 반환합니다.

**numpy.full(shape, fill_value)** : 예시) numpy.full((2, 3), 5)

매개변수
- **shape** : 생성할 배열의 크기나 구조를 지정합니다.
- **fill_value** : 배열을 채울 값입니다.

특징
- 주어진 크기만큼 모든 원소의 값을 주어진 값으로 채워 생성하고 반환합니다.

메소드

**ndarray.astype(dtype)** : 예시) arr.astype(float32)

매개변수
- **dtype** : 변환하고자 하는 대상의 데이터 타입입니다.

특징
- 원소의 타입을 dtype으로 변환시킵니다.



강의 출처 :https://school.programmers.co.kr/learn/courses/16290/16290-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B3%BC%ED%95%99%EC%9D%84-%EC%9C%84%ED%95%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-numpy
