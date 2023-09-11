# x = 10 # immutable
# y = x  # y는 값의 값을 대입 받았으므로 10
# x = 20 # 기존의 x 변수의 값이 변경된 것이 아니라 새롭게 생성 됨
# print(x)  # 20
# print(y)  # 10

"""
튜플이란 ? 변경할 수 없는 시퀀스 자료형 (나머지는 리스트와 동일)
튜플의 정의 : ()소괄호를 사용하거나 생략 할 수 있음, Item들은 콤마 "," 로 구분
"""
# 1. 튜플 만들기
# person = "곰돌이사육사", 20, "서울시 강남구 역삼동"
# print(person)
# 2. 튜플 요소 접근하기
# print(person[0])
# print(person[1])
# 3. 튜플 언패킹
# 이름, 나이, 주소 = person
# print(이름)
# print(나이)
# print(주소)
# 4. 튜플의 언패킹 기능을 이용한 함수 만들기
def get_person() :
    name = "가을"
    age = 23
    addr = "서울시 강남구 역삼동"
    return name, age, addr

result = get_person()  # 언패킹되서 전달되는 반환값을 패킹해서 받음
print(result)

a, b, c = get_person()
print(a)
print(b)
print(c)

tp = 1,1,2,2,2,3,3,3,3
print(tp.count(3))  # 매개변수로 전달한 변수가 몇 번 나오는지 확인 하는 함수 -> 4
print(tp.index(2))  # 매개변수로 전달한 변수의 시작 인덱스를 반환 -> 2
print(len(tp))
#5. 튜플에서 안되는 것 (immutable 특성이기 때문에 삭제 할 수 없음)
# del tp[0]