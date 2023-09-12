"""
고정비용(fix)
가변비용(var)
판매비용(sell)
생산대수(cnt)
"""
# 1번째 방법
#fix, var, sell = map(int,input().split())
# cnt = 0
# while True :
#     if fix + (var * cnt) < sell * cnt : break
#     cnt += 1
#
# print(cnt)

# 2번째 방법
# fix, var, sell = map(int,input().split())
# cnt = 0
# while True :
#     if (cnt > fix) // (sell - var) : break
#     cnt += 1
#
# print(cnt)

# 3번째 방법
fix, var, sell = map(int,input().split())
if sell <= var : print(-1)
else : print(fix // (sell - var) + 1)
