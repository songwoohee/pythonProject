# 인덱싱과 슬라이싱

jumin = "920108-2234567"

gender = jumin[7]   # 성별
year = jumin[:2]   # 출생연도
month = jumin[2:4] # 태어난 달
day = jumin[4:6]   # 태어난 일

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])  # 뒤에서부터 1로 해서 -7
