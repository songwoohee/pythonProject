"""
산술연산자
사칙 연산자(+, -, *, /), //(몫), **(제곱연산자), %(나머지연산자)
증감 연산자는 없다 ex. --i , ++i 기재 시 증감 안됨.
.2f : 출력시 소수점 2자리까지 출력.
파이썬은 상수가 없다. 대문자로 써도 상수 처리가 안됨
"""
i = 10   # 값을 대입할 때 데이터 형이 결정됨, 왜냐하면 파이썬은 데이터형이 없음
j = 3
print(f"덧셈 : {i+j}")
print(f"뺄셈 : {i-j}")
print(f"곱셈 : {i*j}")
print(f"나눗셈 : {i/j}")
print(f"몫 : {i//j}")
print(f"나머지 : {i%j}")
print(f"제곱연산 : {i**j}")

test = "Python !!!"
print(test + " Hello")
print(test + str(100))
print(test * 3)  # test 문자열을 3번 반복 하겠다는 의미.
i += 1    # 밖에서 연산해주고 결과는 출력 문구만
print(f"증감연산자 시험 : {i}")

# 간단 예제 : 파이썬은 변수를 상수로 만드는 방법은 없으며 관례상 변수 이름을 모두 대문자로 표시하면 상수로 간주.
# TAX_RATE = 0.10
# income = int(input("당신의 수입은 얼마 입니까? "))
#
# print(f"당신이 내야할 세금은 {income * TAX_RATE:.2f} 입니다.")

# 관계연산자 : 자바 AND(&&) => 파이썬 and , OR(||) => or, Not(!) => not
x = 10
y = 20
z = 30
rst1 = x > 0 and x > y  # False
rst2 = x > 0 or x > y   # True
rst3 = not( x > 0 or x > y )  # False
print(rst1,rst2,rst3, sep="\t")   # False	True	False

# 다항(3항)연산자
num = int(input("정수 입력 : "))
rst = (num % 2 == 0) and "짝수"  or  "홀수"   # 자바의 > (조건) ? 참 : 거짓 , 동일한 식 또는 람다식은 e -> (e % 2 == 0) and "짝수" or "홀수
print(f"{num}은 {rst} 입니다.")

# 2진수 입력 받기 (0b) 0,1 만
number = 0b101010101
# 8진수 입력 받기 (0o) 7까지
number = 0o1234567
# 16진수 입력 받기 (0x) (0123456789abcdef 총 15개)
number = 0xffffff

