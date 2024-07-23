import sys

n = int(sys.stdin.readline().strip())
n_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
n_list.sort()

# 산술 평균
average = round(sum(n_list)/n)
print(average)

# 중앙값
median = n_list[n // 2]
print(median)

# 최빈값
mode = 0
mode_list = []
mode_dict = dict()
mode_set = set()
# 딕셔너리에 키로 number를 값으로 number의 개수를 저장한다.
for number in n_list:

    if number not in mode_set:
        mode_set.add(number)
        mode_dict[number] = 1
    else:
        mode_dict[number] += 1

# 최빈값 연산, 최빈값이 여러개인 경우 mode_list에 저장
max_count = 0
for number in mode_dict.keys():

    # 첫번째 값인 경우
    if max_count == 0:
        max_count = mode_dict[number]
        mode_list.append(number)
    else:
        if mode_dict[number] == max_count:
            mode_list.append(number)
        elif mode_dict[number] > max_count:
            mode_list.clear()
            mode_list.append(number)
            max_count = mode_dict[number]
mode_list.sort()

if len(mode_list) == 1:
    print(mode_list[0])
else:
    print(mode_list[1])

# 범위
print(n_list[-1] - n_list[0])
