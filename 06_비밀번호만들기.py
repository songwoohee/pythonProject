"""
[문제]
각 사이트 비밀번호 만들기
[규칙]
1. http://naver.com 앞의 http:// 잘라내기
2. 처음 만나는 점 이후 제거
3. 남은 글자 중 처음 3자리 + 글자 개수 + 글자에 포함된 'o'의 개수 + 글자에 포함된 'k'의 개수 + "!" + 자신의 이니셜
"""
file_name = "password.txt"
fd = open(file_name, "wt")

while True :
  url = input("사이트 : ")
  if url == 'exit' : break   # while 탈출문
  my_str = url.replace("http://","")  # 1. http:// 잘라내기
  my_str = my_str[:my_str.index(".")]  # 슬라이싱 :  처음부터 '.' 인덱스 미만까지 잘라냄 / 2. 처음 만나는 점 이후 제거
  password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + ("swh")
  # 3. 남은 글자 중 처음 3자리 + 글자 개수 + 글자에 포함된 'o'의 개수 + 글자에 포함된 'k'의 개수 + "!" + 자신의 이니셜
  print("비밀 번호 : " + password)
  fd.write(password + "\n")  # 파일에 생성된 비밀번호 추가
fd.close()  # while문 빠져 나오면 닫혀야 해서 while문이랑 줄 들여쓰기가 다름
