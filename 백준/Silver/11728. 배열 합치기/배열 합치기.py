import sys

n_a, n_b = map(int, sys.stdin.readline().split())
number_a_list = list(map(int, sys.stdin.readline().split()))
number_b_list = list(map(int, sys.stdin.readline().split()))
sort_list = []

left_a = 0
left_b = 0

while left_a < n_a and left_b < n_b:
    if number_a_list[left_a] < number_b_list[left_b]:
        sort_list.append(number_a_list[left_a])
        left_a += 1
    else: # 둘이 같은 경우도 다음과 같이 처리한다.
        sort_list.append(number_b_list[left_b])
        left_b += 1

sort_list += number_a_list[left_a:]
sort_list += number_b_list[left_b:]

print(" ".join(str(x) for x in sort_list))