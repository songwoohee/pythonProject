"""
예외 처리
예외 상황이 발생 할 가능성이 있는 경우에 대해 try ~ exception을 통해 프로그램의 흐름을 변경 할 수 있습니다.
이를 예외 처리(exception handling)이라 부릅니다.
try except 구문
try:
예외가 발생할 가능성이 있는 코드
except:
예외가 발생 했을 때 실행할 코드
else:
예외가 발생 하지 않았을 때 실행 할 코드
finally:
무조건 실행 하는 코드
"""

# 1번 try ~ execpt

# try:
#     print("나눗셈 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자 입력 : "))
#     num2 = int(input("두 번째 숫자 입력 : "))
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("에러!!! 잘못된 값을 입력 하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print(err)
# else :   # 정상 실행시 호출 조건 분기 되는 위치
#     print("정상 처리 되었습니다.")
# finally: # 정상, 비정상 상관없이 수행되는 위치
#     print("프로그램 실행 완료!!")

# 2번 file이 없어도 오류 발생 안생기고 pass 시켜줌

try :
    score_file = open("score.txt","r", encoding="utf-8")
    print(score_file.read())
    score_file.close()
except FileNotFoundError :
    pass

