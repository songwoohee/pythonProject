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

# 1. 정해진 형식으로 시간을 입력 받아서 출력하기 / map 활용해서 자료형과 받을값 기재 하기 > 시간 쪼개기 split
# hour, min, sec = map(int,input("시간 입력 : ").split(":"))
# if hour > 12 :
#     hour -= 12
#     print(f"오후 {hour:02}시{min:02}분{sec:02}초")
# else :
#     print(f"오전 {hour:02}시{min:02}분{sec:02}초")

# 2. 3개의 정수를 입력 받아 최대값과 최소값 구하기
# a, b, c = map(int,input("정수 입력 : ").split())
# # 최대값
# if a > b :
#     if a > c : print(a)
#     else : print (c)
# else :
#     if b > c : print(b)
#     else: print(c)
# # 최소값
# if a > c :
#     if a > b : print (b)
#     else : print(c)
# else :
#     if b > c : print(c)
#     else : print(a)


# # 3. 주민등록번호를 입력 받아 생년 월일, 성별, 나이 출력하기, 출력예시 920108-1234567
# current_year = datetime.today().year
#
# jumin = input("주민등록번호 : ")
# gender = int(jumin[7])
# year = int(jumin[:2])
# month = int(jumin[2:4])
# day = int(jumin[4:6])
# # 성별 1, 3 남자 / 2, 4 여자
# if gender == 1 or gender == 3 :
#     gender_str = "남성"
# else :
#     gender_str = "여성"
# # 나이 , 1,2 = 1900년대 3,4 = 2000년대
# if gender == 1 or gender == 2 :
#     age = current_year - 1900 - year
# else :
#     age = current_year - 2000 - year
# # 출력 생년월, 성별, 나이 순으로 기재
# print(f"생년월일 : {year:02}년{month:02}월{day:02}일")
# print(f"성별 : {gender_str}")
# print(f"나이 : {age}")

# 4. 개수가 정해 지지 않은 여러 개의 정수를 입력 받아 합계와 평군 구하기 list 사용
score = list(map(int,input("정수 입력 : ").split()))
print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score)/len(score)}")



