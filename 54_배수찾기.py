"""
[문제]
정수 n(0 < n <1000)이 주어졌을 때, n의 배수인지 아닌지를 구하는 프로그램을 작성
[입력]
첫째줄에 n이 주어짐. 한줄에 한개씩 목록에 들어있는 수가 주어짐
이 수는 0보다 크고 10,000보다 작다. 목록은 0으로 끝난다
[출력]
목록에 있는수가 n의 배수인지 아닌지를 구한뒤 출력
[입력 예제]
3
1
7
99
321
777
0
[출력 예제]
1 is NOT a multiple of 3.
7 is NOT a multiple of 3.
99 is a multiple of 3.
321 is a multiple of 3.
777 is a multiple of 3.
"""
# 1. 배수인지 아닌지 구하는 함수 만들기
ls = []
def multiple() :
    num = int(input())
    while True:
        x = int(input())
        if x == 0: break
        ls.append(x)

    for e in ls :
        if e % num == 0 : print(f"{e} is a multiple of {num}")
        else : print(f"{e} is NOT a multiple of {num}")

# 2. n의 정수를 받아서 결과물 출력하기
multiple()

