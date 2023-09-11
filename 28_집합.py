"""
집합이란(set)? 주로 중복 제거를 목적으로 자주 사용 됨.
1. 순서가 보장 되지 않음.
2. 중복 불가
3. mutable 특성을 가짐 (수정 가능)
"""
s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

# 1. 요소의 중복 제거
s3 = set([1,2,3,4,5,1,2,3,4,5,1,2,3])
print(s3)   # {1, 2, 3, 4, 5}

# 2. 합집합 : 한 곳에만 존재해도 모두 불러옴 , 중복 제거
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 3. 교집합 : 집합에서 양쪽 모두에 존재 하는 요소만 선택
print(s1.intersection(s2))  # {4, 5}
print(s1 & s2)  # {4, 5}

# 4. 차집합 :  집합에서 앞에서 뒤를 빼서 남은 앞의 요소만 선택
print(s1.difference(s2))  # {1, 2, 3}
print(s1 - s2)  # {1, 2, 3}

# 중복 제거 로또 번호 만들기
import random

numbers = set()
while True :
    number = random.randrange(1, 46)
    numbers.add(number)
    if len(numbers) == 6 : break;

print(numbers)