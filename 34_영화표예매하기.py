"""
[문제]
1. 메뉴는 [1] 예매하기, [2] 종료하기
2. 사용자로부터 좌석번호(index) 입력받아 예매하는 시스템
3. [V] [V] [V] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
4. 예매 완료 되면 좌석값 1로 변경.
5. 이미 완료된 좌석은 재구매 불가
6. 한 좌석당 예매 가격 12000원
[출력]
프로그램 종료 후, 해당 영화관의 매출액 출력
"""

# 1. 임의로 배열을 만들기(개수를 정할 수 있는 방법) -> list = [] * n 을 하면 n개 만큼 생성된다
ls = [0] * 10
# 2. 총 매출액 함수 만들기
def amount() :
    cnt = 0
    for i in ls :
        if ls == 1 : cnt += 1
    return cnt * 12000

# 3. 선택 받은 좌석 표시
def sel() :
    for i in ls :
        if i == 0 :
            print("[ ]", end=" ")
        else : print("[v]", end=" ")
    print()

# 4. 좌석 예약
def selseat() :
    sel()  # 현재 예약 가능한 좌석 보여주기
    seatpos = int(input("좌석 번호를 입력 하세요 : "))
    if(ls[seatpos - 1] == 0) :  # 선택된 좌석번호는 1번이나 인덱스는 0번부터 시작
        ls[seatpos - 1] = 1
        sel()
    else : print("이미 예약된 좌석 입니다. 다른 좌석을 선택 하세요")

# 5. 출력
while True :
    tickets = int(input("메뉴 [1] 예매하기, [2] 종료하기 : "))
    if tickets == 1 : selseat()
    else :
        print(f"총 금액은 {amount()}원 입니다.")
        break












