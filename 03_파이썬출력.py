# 파이썬의 다양한 출력 방법
name = "우희"
age = 20
gender = "여성"
jobs = "학생"
addr = "서울시 서초구 양재동"

# C언어 스타일 : 서식지정자를 사용 하는 방식
print("=" * 5, "C 스타일 ", "=" * 5)
print("이름 : %s" % name)
print("나이 : %d" % age)
print("성별 : %s" % gender)
print("직업 : %s" % jobs)
print("주소 : %s" % addr)

# 파이썬 스타일 1번 : 3.6 이전 방식
print("=" * 5, "파이썬 1번 스타일 ", "=" * 5)
print("이름과 주소 : {}, {}".format(name, addr))
print("나이 : {}".format(age))

# 파이썬 스타일 2번(현재) : 3.6 이후 방식, f와 {} 사용해서 출력하는 방식
print("=" * 5, "파이썬 2번 현재 스타일 ", "=" * 5)
print(f"이름 : {name}")
print(f"나이 : {age}, 성별 : {gender}, 직업 : {jobs}")

# 자바 스타일 : 문자열 연결 방법 (+)
print("=" * 5, "자바 스타일 ", "=" * 5)
print("이름 : " + name)
# print("나이 : " + age)  # 형이 같아야함, 형이 다르면 출력 에러 나이(문자) + age는 숫자형, 앞에 형 변환 해줘야함
print("나이 : " + (str)(age))
print("주소 : " + addr)

"""
출력시 정렬
< 좌측 정렬
> 우측 정렬, 우측 정렬은 생략 가능 
^ 중앙 정렬 
"""
print("|{:5}|".format(10))  # |{:>5}| 과 동일 , 우측은 생략 가능
print("|{:<5}|".format(10))
print("|{:^6}|".format(10))
"""
출력 
|   10|
|10   |
|  10  |
"""

# 옛날 버전
num = 10
print(f"|{num:<5}|")
print(f"|{num:>5}|")
print(f"|{num:^6}|")

PI = 3.14159265
print(f"{PI:.2f}")  # 소수점 2자리만 3.14
print(f"{PI:}")   # 3.14159265




