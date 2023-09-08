"""
회원 정보 출력
1단계 현재 상태 대로 -> 2단계 함수로 변환
[문제]
회원 정보를 입력 받아 출력
1. 이름 입력
2. 나이 입력 :  1 ~ 199 까지 입력 받고 잘못된 값이 오면 재 입력 요청
3. 성별 입력 : 영문자(M,m 남성),(F,f는 여성), 나머지는 재 입력 요청
4. 직업 입력 : 1(학생),2(회사원),3(주부),4(무직), 나머지 재 입력 요청
5. 결과 한번에 출력
"""
# 1. 함수로 변환 / 함수를 만들어주는 키워드 > def

def input_age() :
    while True:
        age = input("나이를 입력 하세요: ")
        if age.isdigit():
            age = int(age)
            if 0 < age < 200 : return age
        print("나이를 잘못 입력 하셨습니다.")

def input_gender() :
    while True:
        gender = input("성별을 입력 하세요 : ")
        if gender == 'M' or gender == 'm': return "남성"
        elif gender == 'F' or gender == 'f' : return "여성"
        print("성별이 잘못 입력 되었습니다.")

def input_jobs() :
    while True:
        jobs = input("직업을 입력 하세요 : ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0 < jobs < 5 : return jobs
        print("직업을 잘못 입력 하셨습니다.")


def print_info(name, age, gender,jobs) :
    jobs_str = "", "학생", "회사원", "주부", "무직"
    print("=" * 3, "회원정보", "=" * 3)
    return f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}"


# 1. 함수는 선언 이후 호출해야 동작 함
# name = input("이름을 입력 하세요 : ")
# age = input_age()
# gender = input_gender()
# jobs = input_jobs()
# print_info(name, age, gender,jobs)


# 2. 계속 반복 원할시 while문, file 생성해서 넣기
member_info = "member.txt"
fd = open(member_info,"wt", encoding="utf-8")  # encoding="utf-8 한글 안깨지게 해주는 코드

while True :
    name = input("이름을 입력 하세요 (종료시 quit): ")
    if name == 'quit' : break
    age = input_age()
    gender = input_gender()
    jobs = input_jobs()
    rst = print_info(name, age, gender, jobs)
    fd.write(rst + "\n")
fd.close()



# 2. 일반 작성
# name = input("이름을 입력 하세요 : ")
#
# while True :
#     age = input("나이를 입력 하세요: ")
#     if age.isdigit() :      # isdigit() 입력 받은 문자열이 숫자로 구성 되어 있는지 확인
#         age = int(age)
#         if 0 < age < 200 : break
#     print("나이를 잘못 입력 하셨습니다.")  # 첫번째 if문 바깥에 있기 때문에 해당 부분이 아닐 경우 이 부분이 출력.
#
# while True :
#     gender = input("성별을 입력 하세요 : ")
#     if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f' : break
#     print("성별이 잘못 입력 되었습니다.")
#
# while True :
#     jobs = input("직업을 입력 하세요 : ")
#     if jobs.isdigit() :
#         jobs = int(jobs)
#         if 0 < jobs < 5 : break;
#     print("직업을 잘못 입력 하셨습니다.")
#
# if gender == 'M' or gender == 'm' : gen_str = "남성"
# else : gen_str = "여성"
#
# jobs_str = "", "학생", "회사원", "주부", "무직"  # 이렇게 하면 인덱스 0,1,2,3,4 튜플 형태로 인식
#
# print("="*3, "회원정보", "="*3)
# print(f"""
# 이름 : {name}
# 나이 : {age}
# 성별 : {gen_str}
# 직업 : {jobs_str[jobs]}
# """)
#





