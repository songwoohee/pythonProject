# 값을 할당 하는 방법
a = b = c = 1
print(a, b, c)   # 1 1 1

a, b, c = 1, False, "우희"  # 여러 개의 변수를 한번에 대입,
print(a, b, c)    #  1 False 우희, 자료형이 달라도 출력 가능

# 타입 확인
# age = int(input("나이를 입력 하세요 : "))
# print(type(age))

value = 0xffffff
print(value)

# 불리언 타입 : 참과 거짓의 값을 가집니다.
print(bool(1))  # True  값이 있으니 참
print(bool(0))  # False 값이 없으니 거짓
print(bool(-1000)) # True
print(bool(""))   # False 비어 있으니 거짓
print(bool(None))  # False 값이 정해 지지 않았음을 의미 > 거짓

# 문자열 타입
str1 = "Hello Python!!!"
print(str1)
print(str1[0])  # 인덱싱, 0번째 문자열만 가져옴 출력 : H
print((str1)[2:5])  # 2,3,4 인덱스 > llo
print(str1[2:])  # 2번째부터 끝까지 llo Python!!!
print(str1 * 3)  # Hello Python!!!Hello Python!!!Hello Python!!!
print(str1 + "TEST")  # Hello Python!!!TEST

# 형변환 : 형을 다른 형으로 변경, 파이썬은 값이 할당 되는 순간 형이 결정됨. 이후 데이터형을 변경하고자 할 때, 형변환을 사용
print(10 + int("10"))
print("나이 : " + str(30))
print(1 + 3.141592 + float("4.44"))


