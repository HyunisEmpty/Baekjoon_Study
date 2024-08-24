import sys

a, b = map(int, sys.stdin.readline().split())
min_cal = -1

def AtoB(val, target_val, cal):

    global min_cal

    if val == target_val:
        if min_cal == -1:
            min_cal = cal + 1
        else:
            if min_cal > cal:
                min_cal = cal + 1
        return
    elif val > target_val:
        return

    cal += 1

    AtoB(int(str(val) + "1"), target_val, cal)
    AtoB(val * 2, target_val, cal)


AtoB(a, b, 0)

print(min_cal)