"""
[문제]
회원 정보를 입력 받아 출력
1. 이름 입력
2. 나이 입력 :  1 ~ 199 까지 입력 받고 잘못된 값이 오면 재 입력 요청
3. 성별 입력 : 영문자(M,m 남성),(F,f는 여성), 나머지는 재 입력 요청
4. 직업 입력 : 1(학생),2(회사원),3(주부),4(무직), 나머지 재 입력 요청
5. 결과 한번에 출력
"""
name = input("이름을 입력 하세요 : ")

while True:
    age = int(input("나이를 입력 하세요 : "))
    if 1 < age < 200:
        break
    else: print("나이를 다시 입력 하세요")


while True:
    gender = input("성별을 입력 하세요 : ")
    if gender == "M" or gender == "m":
        gender_str = "남성"
        break
    elif gender == "F" or gender == "f":
        gender_str = "여성"
        break
    else: print("잘못 입력 했습니다. 다시 입력 하세요.")

while True:
    job = int(input("직업을 선택 하세요 [1] 학생 [2] 회사원 [3] 주부 [4] 무직 : "))
    if job == 1:
        job_str = "학생"
        break
    elif job == 2:
        job_str = "회사원"
        break
    elif job == 3:
        job_str = "주부"
        break
    elif job == 4:
        job_str = "무직"
        break
    else: print("다시 입력 하세요.")
print()

# 한번에 출력
print("="*5, "회원정보", "="*5)
print(f"이름은 {name} 입니다.")
print(f"나이는 {age}살 입니다.")
print(f"성별은 {gender_str} 입니다.")
print(f"직업은 {job_str} 입니다.")

