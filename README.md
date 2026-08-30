# Numpy

Numpy의 기초와 사용방법을 공부하기 위한 프로젝트입니다.

---

### 목차

* [배열 생성](#배열-생성)
* [인덱싱, 슬라이싱, 불리언/펜시 인덱싱](#인덱싱-슬라이싱-불리언펜시-인덱싱)
* [배열 연산 및 조작 (Arithmetic & Operations)](#배열-연산-및-조작-arithmetic--operations)
* [형태 및 구조 변환 (Shape Manipulation)](#형태-및-구조-변환-shape-manipulation)
* [배열 결합 및 분할 (Combination & Splitting)](#배열-결합-및-분할-combination--splitting)

---

### 배열 생성

---

**numpy.array(object, dtype)** : 예시) numpy.array([1,2,3], dtype = float)  
* 매개변수
  - **object** : NumPy 배열로 변환할 데이터(파이썬 리스트, 튜플 등)입니다.
  - **dtype** : 원소들의 타입을 정할 수 있습니다.(기본값 : int64)
* 속성
  - **.shape** : 배열의 차원별 크기를 튜플형태로 반환합니다.
  - **.ndim** : 배열의 차원(축)의 수를 반환합니다.
  - **.size** : 배열의 전체 원소의 개수를 반환합니다.
  - **.dtype** : 원소의 현재 타입을 반환합니다.
* 메소드
  **ndarray.astype(dtype)** : 예시) arr.astype(float32)  
  * 매개변수
    - **dtype** : 변환하고자 하는 대상의 데이터 타입입니다.  
  * 특징
    - 원소의 타입을 dtype으로 변환시킵니다.
* 특징
  - 배열을 생성하고 반환합니다.
  - 타입은 "numpy.ndarray"입니다.
  - 배열의 원소들은 같은 타입으로 통일 시킵니다.

**numpy.zeros(shape)** : 예시) numpy.zeros([2, 2])  
* 매개변수
  - **shape** : 생성할 배열의 크기나 구조를 지정합니다.  
* 특징
  - 주어진 크기만큼 모든 원소의 값을 0으로 채워 생성하고 반환합니다.

**numpy.ones(shape)** : 예시) numpy.ones([2,3])  
* 매개변수
  - **shape** : 생성할 배열의 크기나 구조를 지정합니다.  
* 특징
  - 주어진 크기만큼 모든 원소의 값을 1로 채워 생성하고 반환합니다.

**numpy.full(shape, fill_value)** : 예시) numpy.full((2, 3), 5)  
* 매개변수
  - **shape** : 생성할 배열의 크기나 구조를 지정합니다.
  - **fill_value** : 배열을 채울 값입니다.  
* 특징
  - 주어진 크기만큼 모든 원소의 값을 주어진 값으로 채워 생성하고 반환합니다.

**numpy.eye(N, M, k)** : 예시) numpy.eye(3, 4, k=0)
* 매개변수
  - **N** : 생성할 행렬의 행의 개수입니다.
  - **M** : 생성할 행렬의 열의 개수입니다.
  - **k** : 1이 채워질 대각선의 위치(Index)를 지정합니다. (기본값: 0)
* 특징
  - 대각선(Diagonal) 성분은 1이고 나머지 성분은 0으로 채워진 단위행렬(Identity Matrix)을 생성하고 반환합니다.
  - N만 주어지면 NxN 정방행렬을 생성합니다.

**numpy.zeros_like(prototype)** : 예시) numpy.zeros_like(arr)
* 매개변수
  - **prototype** : 형상을 복사할 원본 배열 또는 객체입니다.
* 특징
  - prototype을 복사한 배열의 원소들을 0으로 채워 반환합니다.

**numpy.ones_like(prototype)** : 예시) numpy.ones_like(arr)
* 매개변수
  - **prototype** : 형상을 복사할 원본 배열 또는 객체입니다.
* 특징
  - prototype을 복사한 배열의 원소들을 1로 채워 반환합니다.

**numpy.full_like(prototype, fill_value)** : 예시) numpy.full_like(arr, 9)
* 매개변수
  - **prototype** : 형상을 복사할 원본 배열 또는 객체입니다.
  - **fill_value** : 배열을 채울 값입니다.
* 특징
  - prototype을 복사한 배열의 원소들을 fill_value로 채워 반환합니다.

**numpy.arange(start, stop, step)** : 예시) numpy.arange(3, 13, 3)
* 매개변수
  - **start** : 수열의 시작 값입니다.
  - **stop** : 수열의 끝 값입니다.
  - **step** : 값 사이의 간격입니다.
* 특징
  - start부터 stop(이 값은 포함되지 않습니다.)직전까지 등차가 step인 배열을 생성하고 반환합니다.

**numpy.linspace(start, stop, num)** : 예시) numpy.linspace(1, 10, 10)
* 매개변수
  - **start** : 수열의 시작 값입니다.
  - **stop** : 수열의 끝 값입니다.
  - **num** : 생성할 샘플(원소)의 총 개수입니다. (기본값: 50)
* 특징
  - start부터 stop(이 값은 포함되지 않습니다.)직전까지 num개의 원소를 균등한 간격으로 배열을 생성하고 반환합니다.

**numpy.logspace(start, stop, num, base)** : 예시) numpy.logspace(1, 10, 10, base=2)
* 매개변수
  - **start** : 로그스케일의 시작 지점의 지수입니다.
  - **stop** : 로그스케일의 끝 지점의 지수입니다.
  - **num** : 생성할 샘플(원소)의 총 개수입니다. (기본값: 50)
  - **base** : 로그의 밑(base) 값입니다. (기본값: 10.0)
* 특징
  - start부터 stop(이 값은 포함되지 않습니다.)직전까지 num개의 로그스케일 원소를 균등한 간격으로 배열을 생성하고 반환합니다.

**numpy.random.normal()** : 예시) numpy.random.normal(0, 1, 10)
* 매개변수
  - **loc** : 정규 분포의 평균입니다. (기본값: 0.0)
  - **scale** : 정규 분포의 표준편차(standard deviation)입니다. (기본값: 1.0, 음수 불가합니다.)
  - **size** : 반환할 배열의 크기/구조입니다. (기본값: None, 단일 값 반환합니다.)
* 특징
  - 정규 분포를 따르는 난수를 생성하는 함수입니다.

**numpy.random.rand(d0, d1, ..., dn)** : 예시) numpy.random.rand(100)
* 매개변수
  - **d0, d1, ..., dn** : 생성할 배열의 차원별 크기입니다.
* 특징
  - 0 이상 1 미만의 범위에서 균등 분포를 따르는 난수를 생성하고 반환합니다.

**numpy.random.randn(d0, d1, ..., dn)** : 예시) numpy.random.randn(100)
* 매개변수
  - **d0, d1, ..., dn** : 생성할 배열의 차원별 크기입니다.
* 특징
  - 평균이 0이고 표준편차가 1인 표준 정규 분포를 따르는 난수를 생성하고 반환합니다.

**numpy.random.randint(low, high, size)** : 예시) numpy.random.randint(1, 5, 10)
* 매개변수
  - **low** : 최솟값입니다. (high가 지정되지 않은 경우 0부터 low 미만 범위)
  - **high** : 최댓값입니다. (low 이상 high 미만 범위)
  - **size** : 반환할 배열의 크기/구조입니다. (기본값: None)
* 특징
  - 지정한 범위 내에서 균등한 확률로 정수 난수를 생성하고 반환합니다.

**numpy.random.seed()** : 예시) numpy.random.seed(1)
* 매개변수
  - **seed** : 난수 생성기의 시드 값으로 사용할 정수입니다.
* 특징
  - 지정한 시드가 같은 경우 항상 동일한 난수 결과를 얻습니다.
  - 컴퓨터의 난수는 첫 시드에서 특정 계산식(의사 난수 생성 알고리즘)을 거쳐 만들어지는 방식이기 때문입니다.

---

### 인덱싱, 슬라이싱, 불리언/펜시 인덱싱

---

**1차원 배열 인덱싱** : 예시) arr[3]
* **개념** : 배열의 각 요소 자리마다 0부터 시작하는 번호(인덱스)가 부여되어 접근합니다.

**2차원 배열 인덱싱** : 예시) arr[0, 3]
* **개념** : `[행(row), 열(column)]` 형태의 콤마(`,`) 구분 인덱스 접근을 지원합니다.

**슬라이싱 (Slicing)** : 예시) arr[3:8]
* **개념** : `[start:end:step]` 구문을 사용하여 지정한 범위의 요소를 잘라냅니다. (`end` 미포함)
* **주요 형태** : `arr[3:]`, `arr[:7]`, `arr[:-1]` 등

**2차원 배열 슬라이싱** : 예시) arr[:2, 2:]
* **개념** : 행과 열에 동시에 슬라이싱을 적용하여 특정 부분 집합을 추출합니다. (`arr[0, :]`, `arr[:, 1]` 등)

**펜시 인덱싱 (Fancy Indexing)** : 예시) arr[[0, 2, 4]]
* **개념** : 정수 배열이나 리스트를 이용해 비연속적이거나 불규칙한 위치의 요소들을 한 번에 지정하여 접근합니다.
* **혼합 사용** : `arr[[0, 2], 2:]`나 `arr[1:, [2, 3]]`처럼 일반 인덱싱 및 슬라이싱과 혼합할 수 있습니다.

**불리언 인덱싱 (Boolean Indexing)** : 예시) arr[arr > 3]
* **개념** : 참/거짓(`True`/`False`) 배열이나 조건식(`arr > 3`, `arr <= 2`)을 이용해 원하는 요소를 필터링하여 추출합니다.

---

### 배열 연산 및 조작 (Arithmetic & Operations)

---

**배열 간 기본 연산** : 예시) arr1 + arr2 / np.add(arr1, arr2)
* **개념**
  * NumPy 배열 간에는 같은 자리의 요소끼리 연산(`Element-wise`)이 수행되며, 일반 연산자(`+`, `-`, `*`, `/`, `//`, `%`, `**`) 및 전용 함수를 모두 사용할 수 있습니다. (※ 곱셈 `*`와 `np.multiply`는 행렬 내적이 아닌 **요소 간 곱셈**입니다.)
* **주요 연산 함수 및 연산자**
  - **덧셈** : `arr1 + arr2` 또는 `np.add(arr1, arr2)`
  - **뺄셈** : `arr1 - arr2` 또는 `np.subtract(arr1, arr2)`
  - **곱셈** : `arr1 * arr2` 또는 `np.multiply(arr1, arr2)`
  - **나눗셈** : `arr1 / arr2` 또는 `np.divide(arr1, arr2)`
  - **제곱** : `arr1 ** n` 또는 `np.square(arr1)` (각 요소 제곱)
  - **제곱근** : `np.sqrt(arr1)` (각 요소의 제곱근 계산)
  - **몫** : `arr1 // 정수`
  - **나머지** : `arr1 % 정수`

**numpy.dot(arr1, arr2)** : 예시) np.dot(arr1, arr2)
* **매개변수**
  - **arr1, arr2** : 내적(Dot Product)을 계산할 두 배열입니다.
* **특징**
  - **1차원 배열** : 같은 자리 요소끼리 곱한 뒤 모두 합산하여 스칼라 값을 반환합니다.
  - **2차원 배열** : 행렬 곱셈 수행 결과를 반환합니다. (A의 행과 B의 열 간의 1차 내적들의 조합)

**수학 및 반올림 함수** : 예시) np.abs(arr), np.ceil(arr), np.floor(arr), np.round(arr), np.trunc(arr)
* **특징**
  - **`np.abs(arr)`** : 모든 요소의 절댓값을 반환합니다.
  - **`np.ceil(arr)`** : 모든 요소의 올림 값을 반환합니다. (소수점 위로)
  - **`np.floor(arr)`** : 모든 요소의 내림 값을 반환합니다. (소수점 아래로)
  - **`np.round(arr)`** : 모든 요소의 반올림 값을 반환합니다.
  - **`np.trunc(arr)`** : 모든 요소의 소수점을 버립니다.

**배열 집계 및 통계 함수** : 예시) arr.min(axis=0), np.sum(arr)
* **매개변수**
  - **axis** : 연산을 수행할 축입니다. (`0`은 행 방향, `1`은 열 방향, 지정하지 않으면 전체 원소 대상)
* **주요 함수**
  - **`min()` / `max()`** : 최솟값 / 최댓값을 반환합니다.
  - **`sum()`** : 전체 또는 축별 합계를 반환합니다.
  - **`mean()`** : 평균을 구합니다.
  - **`std()`** : 표준편차를 구합니다.
  - **`cumsum()`** : 누적 합계를 계산하여 반환합니다.
  - **`median()`** : 중앙값을 반환합니다.

**배열 비교 연산 및 삼각 함수** : 예시) arr1 == arr2, np.array_equal(arr1, arr2), np.sin(arr)
* **특징**
  - **비교 연산** : `==`, `>`, `<` 등을 통해 배열 간 요소별 비교를 수행해 불리언 배열을 반환합니다.
  - **`np.array_equal(arr1, arr2)`** : 두 배열의 형태와 모든 원소가 완전히 같은지 확인하여 `True`/`False`를 반환합니다.
  - **삼각 함수** : `np.sin(arr)`, `np.cos(arr)`, `np.tan(arr)`을 통해 배열의 모든 요소에 삼각 함수를 적용합니다.
  - **`np.pi`** : 원주율 값(3.141592653589793)을 반환합니다.

**브로드캐스팅 (Broadcasting)** : 예시) arr1 + arr2
* **개념**
  * 크기가 서로 다른 배열 간에 연산이 가능하도록, 작은 배열의 형태를 자동으로 늘려서(확장하여) 같은 크기로 만든 뒤 연산하는 기법입니다.

**벡터 연산과 성능 (Vectorization)** : 예시) np.sum(arr), np.dot(arr1, arr2)
* **개념**
  * 파이썬의 일반 `for`문 대신 NumPy의 내부 최적화된 벡터 연산을 사용하면, C언어 기반의 저수준 연산을 통해 수십 배 이상의 압도적인 속도 향상과 성능 이점을 얻을 수 있습니다.

**배열의 정렬 (Sort)** : 예시) np.sort(arr)
* **특징**
  - **`np.sort(arr)`** : 원소들을 오름차순으로 정렬한 새로운 배열을 반환합니다. (**원본 배열은 변경되지 않음**)
  - **내림차순 정렬** : `np.sort(arr)[::-1]`과 같이 슬라이싱 기법을 함께 사용하여 구현합니다.
  - **2차원 배열 정렬** : `axis=1`(열 방향, 기본값), `axis=0`(행 방향), `axis=None`(1차원 배열로 펼쳐서 전체 정렬)을 지정할 수 있습니다.

**numpy.argsort()** : 예시) np.argsort(arr, axis=1)
* **매개변수**
  - **axis** : 정렬 기준이 되는 축입니다.
* **특징**
  - 정렬을 수행한 후, **정렬되기 전의 원래 인덱스 위치**를 배열 형태로 반환합니다.

---

### 형태 및 구조 변환 (Shape Manipulation)

---

**ndarray.reshape(shape)** : 예시) arr.reshape((3, 4))
* **매개변수**
  - **shape** : 변경하고자 하는 배열의 차원별 크기 튜플입니다.
* **특징**
  - 원본 배열의 전체 요소 개수에 맞게 형태(Shape)를 변경한 새로운 배열을 반환합니다.
  - `-1`을 사용하여 크기를 자동으로 계산할 수 있습니다. (단, 미지정 차원은 최대 1개만 허용되며, 2개 이상 지정 시 `ValueError`가 발생합니다.)

**ndarray.resize(shape)** : 예시) arr.resize(3, 4)
* **매개변수**
  - **shape** : 변경할 배열의 크기입니다.
* **특징**
  - 반환값이 아닌 **원본 배열 자체의 형태를 직접 변경**합니다. reshape과 달리 전체 요소 개수와 정확히 일치하지 않아도 크기 조절이 가능합니다.

**ndarray.ravel()** : 예시) arr.ravel()
* **특징**
  - 다차원 배열을 **1차원 배열**로 펼쳐서 반환합니다.

**numpy.expand_dims(arr, axis)** : 예시) np.expand_dims(arr, axis=1)
* **매개변수**
  - **arr** : 대상 배열입니다.
  - **axis** : 새로 차원을 추가할 축의 위치입니다.
* **특징**
  - 지정한 위치에 새로운 차원(축)을 추가하여 차원을 높입니다.

**numpy.squeeze(arr, axis)** : 예시) np.squeeze(arr, axis=0)
* **매개변수**
  - **axis** : 크기가 1인 제거할 축의 위치입니다. (기본값: 지정하지 않으면 크기가 1인 모든 차원을 축소)
* **특징**
  - 배열의 형태 중 크기가 1인 차원을 제거하여 차원을 낮춥니다.

**전치 행렬 (Transpose)** : 예시) arr.T
* **특징**
  - 행과 열을 서로 맞바꾼 전치 행렬을 반환합니다. (예: 2차원 배열의 행과 열 인덱스를 반전)

---

### 배열 결합 및 분할 (Combination & Splitting)

---

**numpy.insert(arr, index, values, axis)** : 예시) np.insert(arr, 2, 50, axis=1)
* **매개변수**
  - **arr** : 대상 배열입니다.
  - **index** : 삽입할 위치의 인덱스입니다.
  - **values** : 삽입할 값입니다.
  - **axis** : 삽입할 축의 방향입니다. (지정하지 않으면 배열이 1차원으로 평탄화된 후 삽입됨)

**numpy.delete(arr, index, axis)** : 예시) np.delete(arr, 2, axis=1)
* **매개변수**
  - **arr** : 대상 배열입니다.
  - **index** : 삭제할 위치의 인덱스입니다.
  - **axis** : 삭제할 축의 방향입니다. (지정하지 않으면 1차원으로 평탄화된 후 삭제됨)

**numpy.append(arr1, values, axis)** : 예시) np.append(arr1, arr2, axis=0)
* **매개변수**
  - **arr1** : 대상 배열입니다.
  - **values** : 추가할 배열 또는 값입니다.
  - **axis** : 병합할 축의 방향입니다. (지정하지 않으면 1차원으로 평탄화된 뒤 끝에 추가됨)

**numpy.vstack(tup)** : 예시) np.vstack((arr1, arr2))
* **특징**
  - 두 개 이상의 배열을 수직 방향(행 기준, `axis=0`)으로 쌓아서 병합합니다. (`np.append(..., axis=0)`과 동일)

**numpy.hstack(tup)** : 예시) np.hstack((arr1, arr2))
* **특징**
  - 두 개 이상의 배열을 수평 방향(열 기준, `axis=1`)으로 나란히 병합합니다. (`np.append(..., axis=1)`과 동일)

**numpy.concatenate(tup, axis)** : 예시) np.concatenate([arr1, arr2], axis=0)
* **특징**
  - 튜플이나 리스트 형태로 여러 배열을 입력받아 기존 축(`axis`)을 기준으로 연결합니다. `append`와 달리 기본값이 1차원 평탄화가 아니며 반복 사용 시 더욱 효율적입니다.

**numpy.vsplit(arr, indices_or_sections)** : 예시) np.vsplit(arr, 3)
* **특징**
  - 배열을 수직 방향(`axis=0`, 행 기준)으로 지정한 개수나 위치에 맞춰 분할합니다.

**numpy.hsplit(arr, indices_or_sections)** : 예시) np.hsplit(arr, 2)
* **특징**
  - 배열을 수평 방향(`axis=1`, 열 기준)으로 지정한 개수나 위치에 맞춰 분할합니다.

---

강의 출처 :https://school.programmers.co.kr/learn/courses/16290/16290-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B3%BC%ED%95%99%EC%9D%84-%EC%9C%84%ED%95%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-numpy
