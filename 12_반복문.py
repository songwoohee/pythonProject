# 반복문 : 조건이 참인 동안 계속 수행 되는 구문
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# while n :      # 파이썬 정수값이 0이 아니면 참으로 간주.
#     sum += n
#     n -= 1     # 파이썬은 증감 연산자가 없음 (n-- > (x))
# print(sum)

# while True :
#     age = int(input("나이를 입력 하세요 : "))
#     if 0 < age < 200 : break
#     print("나이 입력 범위를 벗어 났습니다.")

"""
for 요소 in 시퀀스 : 시퀀스의 각 요소를 순회하는데 사용 (자바의 향상된 for문과 동일)
"""
# fruits = ["apple","banana","cherry"]
# for e in fruits :
#     print(e)
"""
출력
apple
banana
cherry
"""
# fruits = ["apple","banana","cherry",["seoul","korea"]]
# print(fruits[3][1][0])
# for e in fruits :
#     print(e[0])
"""
리스트에 "apple","banana","cherry" 만 있을때 출력
a
b
c
"""
"""
["apple","banana","cherry",["seoul","korea"]] 있을때 출력
a
b
c
seoul
[ []] > 중괄호 안에 중괄호 문자 전체를 0 인덱스로 인식해서 seoul 출력 
"""
"""
여기에서 korea 'k'만 출력하고 싶으면? 
print(fruits[3][1][0]) > 다차원 배열처럼 출력 하면 k ok 
"""

# str1 = "서울시 강남구 역삼동 KH정보교육원"
# for e in str1:
#     print(e, end="/")   # 서/울/시/ /강/남/구/ /역/삼/동/ /K/H/정/보/교/육/원/

# for 변수 in range (시작값, 종료값, 증감값):
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# for i in range(1, n+1) :  # 1부터 n+1 미만
#     sum += i
# print(sum)

# for문을 역순으로 반복하기
# for i in range(10, -1, -1) : # 10 ~ 0 까지 출력 (종료값이 0 이고 싶으면 0 미만 되어야 하니까 -1을 넣어줌)
#     print(i)

# 이중 for문 별찍기
# n = int(input("정수를 입력 하세요 : "))
# for i in range(0, n) :
#     for j in range(0, n) :
#         print("*", end=' ')
#     print()

#구구단 찍기
# for i in range(2, 10) :  # 2단에서 9단까지
#     for j in range (1, 10) :  # 각 단 1 ~ 9 까지
#         print(f"{i} x {j} = {i * j}")
#     print()

# 홀수/짝수 나누어 찍기
# n = int(input("정수 입력 : "))
# for i in range(0, n) :
#     for j in range(0, n) :
#         if j % 2 == 0 :
#             print("$",end=' ')
#         else: print("*", end=' ')
#     print()

"""
사각형 찍기 
정수값 n을 입력받아 n * n 크기의 행렬을 출력하는 프로그램 작성
값은 1부터 시작 , 이쁘게 찍기 (정렬 맞추기 > i:>3)
"""
# n = int(input("정수 입력 : "))
# for i in range(0, n) :
#     for j in range(1, n+1) :
#         print("*",end = ' ')
#     print()    > 이건 별로 사각형 만드는거

# n = int(input("정수 입력 : "))
# for i in range(1, n * n + 1) :
#     print(f"{i:>3}",end=' ')
#     if i % n == 0 : print()

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
# n = int(input("별 개수 입력 : "))
# for i in range(n):
#     print(" " * (i),end='')  # 공백
#     print('*' * (n- 2 * i))

"""
4번 별찍기
 * * * * *
   * * * *
     * * *
       * *
         *
"""
# n = int(input("별 개수 입력 : "))
# for i in range(n):
#     print(" " * (i),end='')  # 공백
#     print('*' * (n- 1 * i))

"""
문자와 ASCII 코드
chr : 유니코드 값을 입력 받아 그 코드에 해당하는 문자를 출력 
ord : 문자를 유니코드값으로 변환 
"""

for i in range(ord("A"),ord("Z")+1):    # A - Z 까지를 유니코드값으로 변환
    print(chr(i), end=" ")
print()

for i in range(65, 91):  #A:65 Z:90
    print(chr(i), end=" ")
print()

"""
출력
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
"""
