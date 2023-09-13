# [문제]
# 정수 n(0 < n <1000)이 주어졌을 때, n의 배수인지 아닌지를 구하는 프로그램을 작성

n = int(input())
ls = []  # 빈 리스트 생성
while True :  # 0이 입력 되기 전까지 반복 수행
    x = int(input())  # 목록의 수를 입력 받음
    if x == 0 : break # 0이 입력 되면 탈출
    ls.append(x)

for e in ls :
    if e % n == 0 : print(f"{e} is a multiple of {n}")
    else : print(f"{e} NOT a multiple of {n}")

