# 회원 가입을 위한 아이디와 패스워드 입력 받기

user = input("아이디 입력 : ")
if len(user) >= 8 : # 입력 받은 아이디 길이가 10과 같거나 커야함 . 참
      pw = input("비밀번호 입력 : ")
#    if pw.__len__() < 8 or pw.__len__() > 16 : 아래와 동일한 조건문 (내부함수를 이용)
      if len(pw) < 8 or len(pw) > 16 :
         print("비밀번호는 8자에서 16자 사이여야 합니다.")
      elif pw.find(user) >= 0 :  # user = 아이디, find는 찾아주면 무조건 0보다 크다 . 내부에 해당하는 문자열이 있다는 말
         print("비밀번호에 아이디를 포함 시킬 수 없습니다.")
      else :
         print(f"아이디 : {user}")
         print(f"패스워드 : {pw}")
else :
     print("아이디는 반드시 8자리 이상이여야 합니다.")