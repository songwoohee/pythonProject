"""
[문제]
무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력
split(), map()
"""
# (1) 기본 방법

# 1. 입력 받기
# num = list(map(int,input("입력 : ").split()))
# # 2. 짝수 홀수 나누어 담을 빈 리스트 담기
# even = []
# odd = []
# # 3. 홀수 짝수 나누기
# for e in num :
#     if e % 2 == 0 :
#         even.append(e)
#     else : odd.append(e)
# # 4. 출력
# print(f"홀수 : {odd}")
# print(f"짝수 : {even}")


# (2) 람다식
# map : 전달 받은 값을 함수 내부에서 가공해서 반환 (입력 개수와 반환 개수가 동일)
# filter :  전달 받은 값을 함수 내부에서 *조건에 일치*하는 것만 골라서 반환

#num = list(map(lambda e:int(e)*int(e),input("값 : ").split()))  # 람다식
# num = list(filter(lambda e:int(e) % 2 == 0,input("값 : ").split()))  # 람다식

num = list(map(int,input("입력 : ").split()))
odd = list(filter(lambda e:e % 2 == 1, num))
even = list(filter(lambda e:e % 2 == 0, num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")





