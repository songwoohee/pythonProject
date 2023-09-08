"""
외장함수 : 파이썬이 기본적으로 제공, import가 필요함
"""

"""
randint(0, 4) : 0 ~ 4 *사이*의 임의의 정수값이 반환
randrange(0, 4) : 0 ~ 4 *미만*의 임의의 정수값이 반환
"""
# import random
#
# for i in range(100):
#     rand = random.randrange(0, 4)
#     print(rand)

# 현재 시간 가져 오기
from datetime import datetime  # datetime 모듈에서 datetime 함수만 import 함

# print(datetime.today())# 현재 날짜 가져오기  2023-09-08 11:58:11.338955
# print(datetime.today().year) # 현재 연도 가져 오기 2023
# print(datetime.today().month) # 현재 달 가져 오기 9
# print(datetime.today().day) # 현재 일 가져 오기 8
# print(datetime.today().hour) # 현재 시 가져 오기
# print(datetime.today().minute) # 현재 분 가져 오기
# print(datetime.today().second) # 현재 초 가져 오기

# 수학 계산을 위한 math
import math

# print(math.sin(100))  # 사인값 :  -0.5063656411097588
# print(math.cos(100))  # 코사인 0.8623188722876839
# print(math.tan(100))  # 탄젠트  -0.5872139151569291
# print(math.log(100))  # 로그값 4.605170185988092
# print(math.ceil(100.1))  # 무조건 올림 101
# print(math.floor(100.999))  # 무조건 내림 100

# 중복값이 없는 로또 번호 생성하기
import random
print("로도 번호 자동 생성기")
ls = [] # 빈 리스트 만들기
while True :
    rand = random.randrange(1,46)
    if rand not in ls :  # list에 생성된 rand값이 포함되어 있지 않으면
        ls.append(rand)
    if len(ls) == 6 : break
print(ls)
