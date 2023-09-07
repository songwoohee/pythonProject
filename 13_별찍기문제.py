"""
1번 별찍기
*
* *
* * *
* * * *
* * * * *
"""
# n = int(input("별 개수 입력 : "))
# for i in range (n):
#     for j in range(i+1):
#         print("*", end=' ')
#     print()

"""
2번 별찍기 거꾸로 찍기 
* * * * *
* * * * 
* * * 
* * 
*
"""
# 선생님 답
# n = int(input("뒤집어진 역삼각형(왼쪽) : "))
# for i in range(n):
#     for j in range(n-i):  # 처음에 입력한 수가 들어와야 하고 그 다음줄 부터 -1씩 감소
#         print("*", end=" ")
#     print()
# 내가 푼 답
# n = int(input("별 개수 입력 : "))
# for i in range(n,0,-1):  # 받은값, 종료값, 감소값
#     for j in range(i):
#         print("*", end=' ')
#     print()

"""
3번 별찍기 
* * * * *
 * * * * 
  * * * 
   * * 
    *
"""
n = int(input("역삼각형 : "))
for i in range(n, 0, -1):
    for s in range(n - i):
        print(" ", end= "")
    for j in range(i):
        print("*", end=" ")
    print()

"""
4번 별찍기
 * * * * *
   * * * *
     * * *
       * *
         *
"""
# n = int(input("뒤집어진 역삼각형(오른쪽) : "))
# for i in range(n):
#     for s in range(i):   # 공백먼저
#         print(" ", end=" ") # 공백 넣어줌
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
