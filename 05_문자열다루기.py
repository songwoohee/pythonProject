# 인덱싱과 슬라이싱

jumin = "920108-2234567"

gender = jumin[7]   # 성별
year = jumin[:2]   # 출생연도
month = jumin[2:4] # 태어난 달
day = jumin[4:6]   # 태어난 일

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])  # 맨 뒤자리가 -1 , 앞에 0을 썼으므로 0으로 시작 못함

if gender == "1" :
    print("남성 입니다")
else :
    print("여성 입니다.")

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
# a[1] = "L" # 문자열의 요소는 읽을 수는 있지만 변경은 되지 않음. 리터럴 상수

# 대소문자 바꾸기
aa = "Hello Python Program..."   # 리터럴 상수라 원본이 안바뀐다
bb = aa.upper()
print(bb)   # HELLO PYTHON PROGRAM...  # 실제 a에서 바뀌지는 않고 b를 통해 변경 후 출력
print(aa.lower())  # hello python program... # 실제 a가 바뀐게 아니고 lower 를 통해 변경

# 문자열 변경 : replace("")
input_str = "Hello Python Program"  # 리터럴 상수라 원본이 안바뀐다
new_str = input_str.replace("Python","JavaScript")   # 새로운 변수에 replace 를 통해 변환.
print(new_str)  # 출력 Hello JavaScript Program

# 문자열에 포함된 문자 개수 세기, 길이 확인
input_str2 = "Hello Python Program"
print(input_str2.count("lo"))  # 문자열에서 포함된 문자(열)의 개수를 반환
print(len(input_str2))   # 문자의 총 길이를 반환 출력 = 20, 별도의 외부 함수를 사용 하는 방식 (리스트, 문자열 상관없이 길이 반환)

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"길이 : {len(test)}")
print(test.__len__())

print(input_str2.__len__()) # 문자열에 포함된 내장 함수 (문자열내에 있는 메소드 길이를 반환)

"""
문자열 찾기 : find() > 순방향, rfind() > 리버스 방향, index()  
find() : 찾은 문자열의 첫 번째 인덱스를 반환, 못 찾으면 -1을 반환
index() : 찾은 문자열의 첫 번째 인덱스를 반환, 못 찾으면 ValueError 예외 발생 
"""
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))  # 0
print(phrase.rfind("가장"))  # 34 , 뒤에 있는 '가장'을 찾지만 위치에 대한 인덱스는 *앞* 0 부터 시작해서 34가 출력
print(phrase.index("포기"))  # 앞에서부터 센다 출력 9
print(phrase.find("나에게"))  # 없는 글씨라 -1 출력
# print(phrase.index("나에게"))  # 없는 글씨라 ValueError , 에러

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase) # 출력 : 나에게 큰 실수는 포기, 나에게 어리석은 일은 남의 결점 찾기, 나에게 좋은 선물은 용서

# 문자열 연산
print("태양고" + "나희도")
# print("태양고" + 2)  # 문자열과 정수의 연산 불가능
print("안녕하세요 " * 3) # 뒤에 숫자만큼 문자 반복 출력 = 안녕하세요 안녕하세요 안녕하세요
print("안녕하세요", "!"*5, "\n", "\t", "=" * 3, "태양고", "=" * 3, "\n나희도"*3, "입니다.")

"""
출력
안녕하세요 !!!!! 
 	 === 태양고 === 
나희도
나희도
나희도 입니다.
"""

# 문자열 앞 / 뒤 공백 제거 : strip()
input_aa = """
    안녕하세요.
문자열 함수를 알아 봅시다.

"""

print(input_aa.strip())
"""
출력
안녕하세요.
문자열 함수를 알아 봅시다.

"""










