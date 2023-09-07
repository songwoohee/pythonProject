"""
제어문이란? 조건문과 반복문을 의미하며 순차적인 흐름을 제어하는 목적으로 사용 된다.
"""
# n = int(input("정수를 입력 하세요 : "))
# if n > 100 :
#     print(f"{n}은 100보다 큽니다.")
# elif n < 100 :
#     print(f"{n}은 100보다 작습니다.")
# else :
#     print("100과 같습니다.")

# 올려서 써도 됨
# n = int(input("정수를 입력 하세요 : "))
# if n > 100 : print(f"{n}은 100보다 큽니다.")
# elif n < 100 : print(f"{n}은 100보다 작습니다.")
# else : print("100과 같습니다.")

# 조건문에서 문자열 비교

while True :
    season = input("현재 계절을 입력 하세요 : ")
    if season == "spring" :
        print("봄이 왔어요")
        break
    elif season == "summer" :
        print("무더운 여름 입니다")
        break
    elif season == "fall" or season == "autumn" :
        print("가을이 왔어요")
        break
    elif  season == "winter" :
        print("추운 겨울이 왔어요")
        break
    else :
        print("찾는 계절이 없어요")