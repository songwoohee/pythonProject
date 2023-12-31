"""
[문제]
A만원의 고정 비용 = 임대료, 재산세, 보험료, 급여 등
B만원의 가변 비용 = 재료비, 인건비 등
노트북 가격 C만원 책정.
어느 순간 총 수입(판매비용)이 총비용(=고정비용+가변비용) 보다 많아지게 된다.
A,B,C 가 주어졌을 때 손익분기점을 구하는 프로그램을 작성
[입력]
첫째줄에 A,B,C 가 빈 칸을 사이에 두고 순서대로 주어진다.
A,B,C 모두 21억 이하 자연수
[출력]
최초로 이익이 발생하는 판매량 출력. 존재하지 않으면 -1
[입력 예시]
1000 70 170
[출력 예시]
11
"""
# 손익분기점 공식 = 고정비용 / (판매 가격 - 가변 비용)
#                   A   / C - B
# bep = a / (c - b)

# 1. 금액 입력받기
a, b, c = map(int,input("고정 비용, 가변 비용, 판매 가격 순으로 입력 하세요 : ").split())
if  b >= c :
    print(-1)
else:
    n = a / (c - b)
    print(int(n)+1)   # +1을 해주어야 수익이 0 이상으로 존재하게 된다.
   # print(a / (c - b) + 1)


