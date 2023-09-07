print(38)          # 정수형
print("문자열")     # 문자열
print([1, 2, 3])   # 리스트형
print(1+3)
# print(1+"3")        # 파이썬은 문자와 숫자 이어 붙이기 안됨
print("파"+"이"+"썬")  # 문자열 이어 붙이기
print("파""이""썬")
print("파", "이", "썬") # 콤마를 구분자라고 부른다. 기본적으로 한칸의 공백을 가지고 있다
print("파\n\n\n이\t\t썬") # 이스케이프 문자 \n 줄바꿈, \t 탭
print("""
aaaaa
bbbbb
ccccc
""")
print("안녕하세요 라고 \"곰돌이사육사\" 가 말했습니다.")

"""
end 와 sep 옵션 
end : 출력문에서 끝에 자동으로 삽입 되는 문자를 지정하는 옵션 (줄바꿈 문자를 지정>ex.다음줄,$,*..): \n
sep : 출력문의 중간에 삽입 되는 문자를 지정하는 옵션 : 기본은 space  
"""
print("Hello", end="$")
print("Hello", end="*")
print("Hello")
# 출력 Hello$Hello*Hello
print("life","is","too","short", sep="/")
# 출력 life/is/too/short
print("010","1234","5678",sep="-")
# 출력 010-1234-5678

year = 2023
month = 9
day = 6
print(year, month, day, sep="/")








