"""
1. 상근날드 (초급)
[문제]
햄버거 종류는 3가지, 음료는 2가지
햄버거와 음료의 가격이 주어졌을 때, 가장 싼 세트 메뉴에서 50월은 뺀 가격을 출력
[입력]
처음 3개는 햄버거, 다음 2개는 음료수, 가격은 100원이상, 2000원 이하
[출력]
가장 싼 세트 메뉴 - 50
인덱싱 슬라이싱 이용 하기
"""

# 1. 상근날드

# 1. 햄버거와 음료를 입력 받음
list = list(map(int,input("메뉴 입력 : ").split()))
# 2. 햄버거 음료수 최소값 구하기
min_b = min(list[:3])
min_d = min(list[3:5])
# 3. 출력
print(f"가격은 {min_b + min_d - 50} 입니다.")

