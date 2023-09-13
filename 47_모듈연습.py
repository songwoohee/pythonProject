# import math   # math 모듈을 사용하기 위해서 import 함
# print(math.sin(1))
# import math
# 모듈내에 함수(메소드)중 특정한 함수만 가져오고자 하는 경우
# from math import sin, cos, tan   # math 함수중 sin, cos, tan 이 3가지만 가져옴(그 외 함수는 이용 안됨)
# print(sin(1))
# print(cos(1))
# print(tan(1))

# 모듈을 가져올 때 충돌이나 긴 이름을 간결하게 사용하기 위해 별칭을 부여 = as / (별칭을 부여하면 원래 이름은 사용이 안됨
# import math as m
# print(m.cos(1))
# # print(math.tan(1))  # 별칭을 부여해서 출력시 오류
#
# # sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈
# import sys
# print("명령 줄 인수 : ", sys.argv)
# # 출력 : 명령 줄 인수 :  ['D:\\dev\\work_python\\pythonProject\\47_모듈연습.py']
# print("실행 경로 : ", sys.path[0])
# # 출력 : 실행 경로 :  D:\dev\work_python\pythonProject
# sys.stdout.write("Hello, world !!! \n")
# # print 처럼 출력 해줌 Hello, world !!
# sys.stderr.write("Error !!! \n")
# sys.exit(0)  # 강제 종료

# os 모듈 : 운영체제와 상호 작용 하기 위한 기능을 제공 (파일 시스템 접근, 환경 변수 제어, 프로세스 관리 등)
import os
cwd = os.getcwd()  # 현재 작업 디렉토리
print("현재 작업 디렉토리 : ", cwd)
# 현재 작업 디렉토리 :  D:\dev\work_python\pythonProject
# 디렉토리 생성
# is_dir : os.mkdir("testDir")  # 디렉토리 생성 (파일이 생성됨)
is_dir = os.path.isdir("testDir")
if not is_dir : os.mkdir("testDir")  # testDir 없으면 파일 생성해라. 있으면 아무 생성도 오류도 없음
is_file = os.path.isfile("score.txt")
print(is_file)  # True

os.system("dir")