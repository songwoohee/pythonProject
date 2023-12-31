"""
[문제]
요금제 2가지 종류가 있다.
1. 영식 요금제
30초마다 10원씩 청구.
즉 29초 또는 그보다 적은 시간 통화 하면 10원. 30초부터 59초는 20원
2. 민식 요금제
60초마다 15원씩 청구.
즉 59초 또는 그보다 적은 시간 통화 하면 15원. 60초부터 119초는 30원
> 통화 시간 목록이 주어 질때 어느 요금제를 사용 하느 것이 저렴한지 출력
[입력]
저번 달 이용한 통화의 개수 N이 주어짐. N은 20보다 작거나 같은 자연수.
둘째 줄에 통화 시간 N이 주어짐. 통화시간은 10,000보다 작거나 자연수
[입력 예제]
3
40 40 40
[출력]
첫째 줄에 싼 요금제의 이름을 출력. 영식은 Y, 민식은 M , 요금이 모두 같으면 영식을 먼저 쓰고 그 다음 민식
[출력 예제]
M 45
"""

# list = 크기 상관없이 받을 수 있음. 갯수가 정해져있지 않다.

# n = int(input())  # 통화 횟수
# call = list(map(int, input().split()))  # 통화 횟수에 대한 통화 시간
# y_pay = m_pay = 0
# for i in range(n):
#     y_pay += (call[i] // 30) * 10 + 10 # 30초로 나누고 남은 몫 > 1번, 2번
#     m_pay += (call[i] // 60) * 15 + 15
#
# if y_pay > m_pay :
#     print("M", m_pay)
# elif y_pay < m_pay :
#     print("Y", y_pay)
# else:
#     print("YM", y_pay)


"""
대소문자 바꾸기
[문제]
영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
"""
# rst = ""  # 변수 만들어줘야 오류 안남
# for e in input():    # 향상된 for문 : for i in 자료형 > input 넣으면 입력 받은 문자열만큼 계속 돌려준다(자동 순회)
#     if e.islower():
#         rst += e.upper()
#     else :
#         rst += e.lower()
# print(rst)

"""
숫자의 개수
[문제]
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 ,A × B × C = 150 × 266 × 427 = 17037300 ,계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 
> 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력 
"""
a, b, c = map(int, input("정수 3개 입력 : ").split())
total_val = str(a * b * c)   # a * b * c 결과를 문자열로 반환
for i in range(10):
    print(total_val.count(str(i)))  # 해당 문자의 개수 반환







