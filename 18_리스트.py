"""
리스트 :  크기가 정해지지 않은 요소들에 대해 값을 저장하기 위한 자료형
1. 아무 자료형으로 와도 된다.
2. 중첩 사용이 가능하다. [[},[],[]] / [[[]]] 등
3. 뮤터블 객체(읽고 쓰기가 가능)
"""

number = [1,2,3,4,5,6]
fruits = ["apple","banana","orange"]
mixed = [1, True, "seoul", 12.33333]
dup = [[1,2,3,4],["apple","키위"]]

# 변수와 리스트를 비교해보기
kor, eng, mat = map(int,input("성적 입력 : ").split())
print(sum([kor,eng,mat]))   # 변수 개수와 맞게 입력해야 오류가 안남

# 리스트는 성적의 개수에 상관없이 입력 받을 수 있음.
score = list(map(int,input("성적 입력 : ").split()))
print(sum(score))
print(sum(score) / len(score))

# 인덱싱
str_name = ["seoul", "gangnam", "suwon", "incheon"]
print(str_name) # 리스트 전체 출력 ['seoul', 'gangnam', 'suwon', 'incheon']
print(str_name[1])  # 1번째 요소 출력 gangnam
print(str_name[1][2]) # 1번쨰 요소의 2번째 문자 출력 n

# 슬라이싱
slice = str_name[1:3]  # 1번에서 3번 미만까지 잘라냄
print(slice)   # ['gangnam', 'suwon']
print(len(slice[0]))   # 7 : 슬라이싱 해서 가져온 리스트 0번 인덱스 gangnam 에 대한 길이 반환함

primes = [2,3,5,7]
print(primes[0])  # 2
print(primes[-1]) # 7
print(primes[-2:]) # [5, 7]

# 리스트 연산자 : 연결(+), 반복(*), len()
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a + list_b)
print(list_a * 3)
print(len(list_a + list_b))

# 리스트 요소 추가하기
# append() : 리스트 맨 마지막에 추가
# insert(index, 값) : 해당 인덱스에 값을 삽입
list_a = [1,2,3]
list_a.append(4)
list_a.append(5)
list_a.insert(1,10)
print(list_a)

# 리스트 제거하기 : pop(), remove(), clear(), del 리스명[인덱스]
# pop() : 인덱스가 없으면 마지막 인덱스의 값을 반환하고 삭제, 인덱스가 있으면 해당 위치의 값을 삭제
# remove(값) : 해당하는 값을 제거 , 만약 동일한 값이 여러개인 경우 낮은 인덱스 값 제거
# clear() :  모든 값을 삭제, 리스트는 지우지 않음
list_all = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2 ,3 ,4, "a", "b", "c","d", "korea"]
print(list_all.pop()) # 인덱스가 없으면 마지막 값 반환하고 삭제 -> korea
print(list_all)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd']
print(list_all.pop(5))  # 해당 인덱스의 값을 삭제하면서 어떤 값인지 보여줌 -> 5
print(list_all) # [0, 1, 2, 3, 4, 6, 7, 8, 9, 'a', 'b', 'c', 'd']
list_all.remove(2)  # 해당값을 제거 하는데 보여주지 않음. 즉 반환값이 없다.
print(list_all)    # [0, 1, 3, 4, 6, 7, 8, 9, 0, 1, 2, 3, 4, 'a', 'b', 'c', 'd']
del list_all[3]    # 해당 인덱스의 값을 지움 (pop과 비슷함)
print(list_all)
list_all.clear()
print(list_all)   # [] -> 값만 삭제

# # 중복제거 not in
my_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,1,2,3,4]
new_list = []
for e in my_list:
    if e not in new_list:
        new_list.append(e)
print(new_list)

# map(반환 함수, 입력 자료형), filter(반환 함수, 입력 자료형) 동작 확인 하기
num = list(map(int,input("값 : ").split()))
num = list(map(lambda e:int(e)*int(e),input("값 : ").split()))  # 람다식
num = list(filter(lambda e:int(e) % 2 == 0,input("값 : ").split()))  # 람다식
print(num)

# 리스트의 원소 스캔 하기
x = ["John", "George","Paul","Ringo"]
for e in x:  # 향상된 for문과 비슷한 형태
    print(e)

# range로 돌려보기
for i in range(len(x)):  # 범위 기반 for문 (초기값,최종값,증감값)
    print(x[i])


