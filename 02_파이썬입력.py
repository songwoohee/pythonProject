"""
파이썬 입력
사용자의 입력을 받아 그 값을 프로그램에서 사용 하고자 할 때 input() 함수를 사용
input 함수를 통해서 입력 받은 데이터는 *문자열*로 반환, 원하는 데이터형으로 변환이 필요
"""
# print("이름을 입력 하세요 : ", end=" ")
# name = input()
# print(f"당신의 이름은 {name} 입니다.")

# 다 간결한 방법 > input에 넣어 버리기
# name = input("이름을 입력 하세요 : ")
# age = int(input("나이를 입력 하세요 : "))
# addr = input("주소를 입력 하세요 : ")
# jobs = input("직업을 입력 하세요 : ")
# score = float(input("점수를 입력 하세요 : "))
# print("="*10)
#
# print(f"안녕하세요? '{name}' 님")
# print(f""" 당신의 주소는 {addr}이고,
# 직업은 {jobs}이며,
# 나이는 {age} 입니다.
# 성적은 {score} 입니다.
# """)

# split 함수는 기본적으로 공백 기준, 변수 2개 선언 하면 동시에 2개를 입력 받을 수 있다.
# str1, str2 = input("이름과 주소를 입력 : ").split()
# print(str1, str2)
# """
# 출력
# 이름과 주소를 입력 : 우희 서울시
# 우희 서울시
# """

# map은 입력 받은 개수만큼 그대로 출력 해준다. map(받고 싶은 자료형이나 함수(int..), 받을 값)
# kor, eng, mat = map(int, input("국어 영어 수학 입력 : ").split())
# print(kor, eng, mat)

# val = list(map(int, input("성적 입력 : ").split()))   # 값을 무한대로 받을 수 있다.
# print(val)
# """
# 출력
# 성적 입력 : 100 30 89 97 85 78
# [100, 30, 89, 97, 85, 78] > 리스트 형태로 반환
# """

# hour, min, sec = input("시:분:초 : ").split(":")
# print(f"{hour}시 {min}분 {sec}초 입니다.")

# 시간은 24시간제 이며 ':' 기준으로 입력 받은 후 오전과 오후로 출력하도록 변경
hour, min, sec = map(int,input("시간 입력 : ").split(":"))
if(hour > 12) :
    hour -= 12
    print(f"오후{hour:02}시{min:02}분{sec:02}초")
else :
    print(f"오후{hour:02}시{min:02}분{sec:02}초")
"""
출력
시간 입력 : 23:03:05
오후11시03분05초
"""






