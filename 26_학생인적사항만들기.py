"""
1. 딕셔너리를 사용해 학생의 인적 사항 등록, 검색, 저장, 불러오기 기능 구현
2. 저장은 Rest API의 기본 형태인 JSON으로 저장 및 불러오기 (웹에서 API의 기본 포맷)
3. 함수로 구현
"""
import json  # json 형식으로 데이터를 저장하고 불러오기 위해 json 모듈을 import
# 1. 학생 정보를 저장할 빈 딕셔너리 생성
student_map = {}
# 2. 함수 만들기 def
# (1) 학생 정보 등록
def reg_student() :
    student_id = input("학번 입력 : ")
    name = input("이름 입력 : ")
    addr = input("주소 입력 : ")
    student_map[student_id] = {"이름" : name, "주소" : addr}  # 값을 딕셔너리에 추가
    print(f"{name}님의 정보가 등록 되었습니다.")

# (2) 학생 정보 검색
def search_student() :
    student_id = input("검색할 학번 입력 : ")
    student_info = student_map.get(student_id)
    if student_info :
        print(f"학번 : {student_id}")
        print(f"이름 : {student_info['이름']}")
        print(f"주소 : {student_info['주소']}")
    else :
        print("해당 학번의 학생 정보를 찾을 수 없습니다.")

# (2-1) 학생 정보 저장 (파일 생성 후 저장) / with : close문 생략 가능
def save_student() :
    with open("student.json", 'w', encoding='utf-8') as file :
        json.dump(student_map, file, ensure_ascii=False)
    print("학생 정보가 저장 되었습니다.")

# (2-2) JSON 파일을 불러 옴
def load_student() :
    try:
        with open('student.json', 'r', encoding='utf-8') as file :
            student_map.clear()  # 현재 메모리에 있는 데이터 초기화
            student_map.update(json.load(file))
        print("학생 정보를 불러왔습니다.")
    except FileExistsError:
        print("학생 정보가 저장된 파일을 찾을 수 없습니다.")


# (3) 학생정보 변경
def modify_student() :
    student_id = input("수정할 학번을 입력 하세요 : ")
    student_info = student_map.get(student_id)  # 학번을 키로 해서 해당하는 값(이름과 주소로 구성된 딕셔너리)
    if student_info :
        name = input("새로운 이름 입력 : ")
        addr = input("새로운 주소 입력 : ")
        student_info['이름'] = name
        student_info['주소'] = addr
        print(f"{name}님의 정보가 수정 되었습니다.")
    else : print("해당 학번의 학생 정보를 찾을 수 없습니다.")

# (4) 학생 정보 삭제
def delete_student() :
    student_id = input("삭제할 학번을 입력 하세요 : ")
    if student_map.get(student_id) :
        del student_map[student_id]  # 키로 해당 딕셔너리 삭제
        print("학생 정보가 삭제 되었습니다.")
    else : print("해당 학번의 학생 정보를 찾을 수 없습니다.")

# (5) 학생 정보 보기
def view_all_student() :
    for student_id in student_map :
        student_info = student_map.get(student_id)  # = tudent_map[student_id] 동일
        print(f"학번 : {student_id}")
        print(f"이름 : {student_info['이름']}")
        print(f"주소 : {student_info['주소']}")

# (6) 출력
while True :
    print("="*5, "학생 정보 관리 프로그램", "="*5)
    choice = input("[1] 등록 [2] 검색 [3] 수정 [4] 삭제 [5] 전체 보기 [6] 저장 [7] 불러오기 [8] 종료 : ")
    if choice == "1" : reg_student()
    elif choice == "2" : search_student()
    elif choice == "3" : modify_student()
    elif choice == "4" : delete_student()
    elif choice == "5" : view_all_student()
    elif choice == "6" : save_student()
    elif choice == "7" : load_student()
    elif choice == "8" : break
    else : print("선택한 메뉴가 없습니다.")
