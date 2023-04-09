import sys

str = sys.stdin.readline().strip()
target_str = sys.stdin.readline().strip()

count = 0
target_count = 0

# 브루트포스 알고리즘
while count < len(str) - len(target_str) + 1:
    if str[count:count + len(target_str)] == target_str:
        target_count += 1
        count += len(target_str)
    else:
        count += 1

print(target_count)