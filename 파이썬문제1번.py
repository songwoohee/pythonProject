"""
[문제]
1. 정해진 형식으로 시간을 입력 받아서 출력하기
  입력 형식 : 22:5:5 -> 오후 10시 05분 05초
2. 3개의 정수를 입력 받아 최대값과 최소값 구하기
  (조건문)
3. 주민등록번호를 입력 받아 생년월일, 성별, 나이 출력하기
  current_year = datetime.today().year
4. 개수가 정해 지지 않은 여러 개의 정수를 입력 받아 합계와 평군 구하기
  list 사용
"""
from datetime import datetime

# 1. 정해진 형식으로 시간을 입력 받아서 출력하기
# hour, min, sec = map(int,input("시간 입력 : ").split(":"))
# if(hour > 12) :
#     hour -= 12
#     print(f"오후{hour:02}시{min:02}분{sec:02}초")
# else :
#     print(f"오전{hour:02}시{min:02}분{sec:02}초")

# 2. 3개의 정수를 입력 받아 최대값과 최소값 구하기
a, b, c = map(int,input("정수 입력 : ").split())
if a > b :
    if a > c : print(a)
    else : print(c)
else :
    if b > c : print(b)
    else : print(c)

    if a > c :
        if a > b : print(b)
        else : print(c)
    else :
        if b > c : print(c)
        else : print(a)

# 3. 주민등록번호를 입력 받아 생년월일, 성별, 나이 출력하기
jumin = input("주민등록번호 입력 : ")  # 입력예시 : 9201081234567
print(jumin)

gender = int(jumin[6])
year = int(jumin[:2])

if gender == 1 :
    print("성별 : 남자")
else :
    print("성별 : 여자")

print("생년월일 : " + jumin[:6])

now = datetime.today().year

if gender == 1 or gender == 2 :
    age = now - 1900 - year
else :
    age = now - 2000 - year

print(f"나이 : {age}")







