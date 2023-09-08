"""
내장함수 : 파이썬이 기본적으로 제공, import가 필요 없음
max, min, divmod, sort
"""

# 큰 값, 작은 값 찾기
print(max(1, 2, 3, 777, 86, 159))
print(min(1, 2, 3, 87, 95, 756))

# 총 합 구하기
print(sum([1, 2, 3, 777, 86, 159]))  # 리스트에 대한 총 합
print(sum((1, 2, 3, 777, 86, 159)))  # 튜플에 대한 총 합
num = list(map(int,input("정수값 입력 : ").split()))
print(f"입력 받은 수의 총 합 : {sum(num)}")
print(f"입력 받은 수의 총 평균 : {sum(num)/len(num)}")

# 몫과 나머지 구하기 : divmod(x, y)
print(f"몫과 나머지 : {divmod(10, 4)}")  # 튜플의 동작 원리, 두 개의 반환값으로 받음

# 여러개의 값을 한번에 입력 받아 리스트로 만들고,
# 1. 최대값 & 최소값 & 합계 & 평균 2. 몫과 나머지 (나누는 수 5) 출력해보기
n = list(map(int,input("정수값 입력 : ").split()))
print(f"""
최대값 : {max(n)}
최소값 : {min(n)}
합계 : {sum(n)}
평균 : {sum(n)/len(n)}
""")
print(f"몫과 나머지 : {divmod(sum(n),5)}")

# 정렬
my_list = [1, 2, 3, 1000, 254, 777, 86, 159]
print(sorted(my_list, reverse=True)) # 내림차순
print(sorted(my_list))               # 오름차순



