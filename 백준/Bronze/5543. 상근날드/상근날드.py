import sys

buger_list = []
soda_list = []

for _ in range(3):
    buger_list.append(int(sys.stdin.readline().strip()))

for _ in range(2):
    soda_list.append(int(sys.stdin.readline().strip()))

answer = float("inf")
for i in range(3):

    for j in range(2):

        answer = min(buger_list[i] + soda_list[j] - 50, answer)

print(answer)