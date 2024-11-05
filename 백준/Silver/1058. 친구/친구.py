import sys

n = int(sys.stdin.readline().strip())
n_list = [set() for _ in range(n)]      # 친구 저장 하는 집합
n_list2 = [set() for _ in range(n)]     # 친구의 친구 저장 하는 집합

# 친구 조사
for now_set in n_list:

    friend_str = sys.stdin.readline().strip()

    for j in range(len(friend_str)):

        if friend_str[j] == "Y":
            now_set.add(j + 1)

# 곂지인 조사
max_len = 0
for i in range(len(n_list)):

    now_set = n_list[i]

    for j in range(len(n_list)):
        if i != j:
            target_set = n_list[j]
            if j + 1 not in now_set and i + 1 not in target_set:      # A와 A는 친구가 아니다. 스스로를 비교하진 않는다. 또한 직접적인 친구가 아니다,
                if len(now_set&target_set) != 0:    # 곂지인이 존재 한다면

                    n_list2[i].add(j+1)
                    n_list2[j].add(i+1)

    max_len = max(max_len, len(n_list[i]) + len(n_list2[i]))

print(max_len)