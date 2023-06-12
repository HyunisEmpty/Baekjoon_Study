import sys

n = int(sys.stdin.readline().strip())

ans = 1
for i in range(1, n+1):
    ans = ans * i

index = len(str(ans)) - 1
ans = str(ans)
count = 0
while True:
    if ans[index] == "0":
        count += 1
        index -= 1
    else:
        break

print(count)