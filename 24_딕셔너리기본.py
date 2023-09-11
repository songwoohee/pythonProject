"""
딕셔너리 : 키와 값이 한쌍으로 이루어진 구조 (자바의 맵과 동일)
1. 중괄호{} 감싸서 선언, 쉼표(,)로 구분
2. 키와 값은 콜론(:)으로 구분
"""
coffee_menu = {"Americano" : 2500, "Espresso" : 2500, "Latte" : 4000, "Mocha" : 4500}
tea_menu = {"Black tea" : 4000, "Green tea" : 4000, "Milk tea": 3500}
food_menu = {"Cake" : 5000, "Bakery" : 6000, "Icecream" : 7000}

print(coffee_menu)
print(tea_menu)
print(food_menu)
print(coffee_menu["Americano"])  # 키로 값을 확인하는 방법
print(coffee_menu.get("Latte"))  # get 메소드로 키를 넣어서 값을 확인하는 방법

# update 메서드(함수) : 딕셔너리의 데이터를 한꺼번에 변경
dict = {"곰돌이" : 90, "안유진" : 88, "장원영" : 77 }
dict.update({"곰돌이" : 100, "장원영" : 100})
print(dict)

# 정보 얻기 : keys(), values(), items()
dict1 = {"Java" : 80, "JavaScript" : 88, "html": 70}
print(dict1.keys()) # 딕셔너리에 포함된 키를 확인 dict_keys(['Java', 'JavaScript', 'html'])
print(dict1.values()) # 딕셔너리에 포함된 값을 확인 ict_values([80, 88, 70])
print(dict1.items())  # 키와 값 확인 dict_items([('Java', 80), ('JavaScript', 88), ('html', 70)])

# 키의 포함 여부 확인
print("html" in dict1) # 딕셔너리에 키가 포함 되어 있는지 확인 True
print("Python" in dict1) # False
print(dict1.get("Python"))  # 없으면 None
print(dict1.get("JavaScript"))  # 있으면 키에 해당하는 값을 보여줌 88

# 반복문에 키를 사용해 값을 가져오기
for key in coffee_menu :   # 딕셔너리를 for문으로 순회하면 요소의 키값을 자동으로 접근할 수 있음
    print(key, ":", coffee_menu[key])
# 출력
# Americano : 2500
# Espresso : 2500
# Latte : 4000
# Mocha : 4500

