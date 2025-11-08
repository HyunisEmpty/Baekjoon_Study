a, b, c, m = map(int, input().split())

fatigue = 0   # 현재 피로도
work = 0      # 총 일한 양

for hour in range(24):  # 하루 24시간
    if fatigue + a <= m:  # 피로도가 최대치를 넘지 않으면
        fatigue += a
        work += b
    else:  # 넘으면 쉬기
        fatigue = max(0, fatigue - c)

print(work)
