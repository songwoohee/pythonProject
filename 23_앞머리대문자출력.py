"""
앞머리 대문자 출력 Knuth-Morris-Pratt -> KPM, Mirko-Slavko -> Ms
"""

upper_str = ""
for e in input() : # 입력 받은 수만큼 자동 순회
    if e.isupper() :
        upper_str += e
print(upper_str)