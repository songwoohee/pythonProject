"""
저항 (중급)
[문제]
색 3가지 입력, 처음 색 2개는 저항의 값이고 마지막 색은 곱해야 하는 값
[  색  ] [ 값 ]  [ 곱 ]
 black     0      1
 brown     1      10
 red       2      100
 orange    3      1,000
 yellow    4      10,000
 green     5      100,000
 blue      6      1,000,000
 violet    7      10,000,000
 gray      8      100,000,000
 white     9      1,000,000,000
예를 들어, 저항의 색이 yellow, violet, red였다면 저항의 값은 4,700이 된다.
첫번째 색상은 10의 자리수, 두번째 수는 1의 자리수, 세번째 자리수는 곱해야 하는 수(1, 10, 100..)
"""

# 2. 저항

# 1. 받을값 정의
color = "black","brown","red","orange","yellow","green","blue","violet","gray","white" # 튜플
# 2. 인덱스 이용해서 값 받기
f_name = color.index(input())  # input으로 입력 받은 문자열이 color 튜플내에 인덱스로 반환
s_name = color.index(input())
t_name = color.index(input())
print(int(str(f_name)+str(s_name)) * (10 ** t_name))

