print("Hello world")
print("Hello world")
print(100)
print(33.33)
print(100 + 23)

# 변수를 선언하고 값을 대입
num = 100  # 데이터형은 값이 대입되는 순간에 결정 남
print(num)
num = "100"

# 주석 한번에 잡기
"""
여기는 범위 주석 구간 입니다. 

"""

# 변수 활용
name = "우희"
email = "wuheee@naver.com"
age = 25
addr = "서울시 강남구 서초동"

# print 한번에 출력 하기
print(f"""
이름 : {name}
이메일 : {email}
나이 : {age}
주소 : {addr}
""")

# 파이썬은 boolean 값 대문자로 시작 /  줄 들여쓰기 안지키면 에러(탭 사용 권장 4칸)
isAdult = True
if isAdult:
    print("나는 성인 입니다.")
else:
    print("나는 성인이 아닙니다.")

"""
작성자 : 우희
수정 날짜 : 2023.09.06
"""

'''
작성자 : 우희
수정 날짜 : 2023.09.06
'''
print([1, 2, 3])  # 리스트 출력
