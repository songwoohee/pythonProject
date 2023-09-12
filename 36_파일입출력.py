"""
파일쓰기 : 파일을 읽거나 쓰기 위해서는 반드시 open() 해야함
파일객체 = open(파일명, 파일모드, 인코딩)
파일명 : 파일 경로 + 파일명 (파일 경로를 입력하지 않으면 현재 위치에 저장)
파일모드 : r(읽기), w(쓰기), a(append = 추가, 파일이 없으면 생성하고 추가가 됨. 있으면 파일의 마지막에 추가)
encoding=”utf-8”은 한글 깨짐 방지를 위한 인코딩
"""
# score_file = open("score.txt","w",encoding="utf-8")
# print("수학 : 50", file=score_file)
# print("영어 : 90", file=score_file)
# score_file.write("국어 : 98" + "\n")
# score_file.write("과학 : 45" + "\n")
# score_file.close()

"""
파일 읽기 
read() : 파일내의 모든 내용을 읽어 하나의 문자열로 반환 
readline() : 해당 파일의 내용을 한 라인씩 읽어 들여 문자열로 반환, 더 이상 읽을 내용이 없으면 None 반환
readlines() :  해당 파일의 모든 라인을 순서대로 읽어 각각의 라인을 하나의 요소로 저장하는 리스트를 반환 
"""
# 1번째 방법
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# 2번째 방법
# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline()  # 한줄씩 읽음
#     if not line : break  # 더이상 읽을 라인이 없으면 None 값으로 확인되고 None은 거짓이다.
#     print(line, end="")  # 한줄씩 읽어서 출력하기 때문에 줄바꿈 문자가 포함되어 있음.
# score_file.close()
"""
출력
수학 : 50
영어 : 90
국어 : 98
과학 : 45
"""

# 3번째 방법
# score_file = open("score.txt", "r", encoding="utf-8")
# lines = score_file.readlines()  # 해당 파일의 모든 라인을 순서대로 읽어서 리스트 생성
# for e in lines :
#     print(e, end="")
# score_file.close()
"""
출력
수학 : 50
영어 : 90
국어 : 98
과학 : 45
"""
# 4. with 키워드 사용하기 : open() 이후에 자동으로 close()를 호출해 주는 기능
# with open("score.txt","r",encoding="utf-8") as score_file :
#     print(score_file.read())
#
# print("프로그램의 끝")

"""
출력
수학 : 50
영어 : 90
국어 : 98
과학 : 45
(이 부분에서 자동으로 close 됨) 
프로그램의 끝
"""

# pickle : 파이썬 객체를 직렬화(serialize)하고 역직렬화(deserialize)하기 위한 모듈

# 1. 객체를 직렬화하여 파일에 저장하기
import pickle
# date = {"name" : "우희", "age" : 22, "addr" : "서울시 강남구 역삼동"}
#
# with open("date.pickle", "wb") as file :
#     pickle.dump(date, file)
# 2. 파일에서 객체를 역직렬화 하여 복원하기
with open("date.pickle", "rb") as file :
    restored_data = pickle.load(file)

print(restored_data)