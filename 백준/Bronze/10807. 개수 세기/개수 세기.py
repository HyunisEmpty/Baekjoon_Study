#10807 
N = int(input())
numbers = list(map(int, input().split()))
v = int(input())

a = 0
for num in numbers:
    if num == v:
        a += 1
print(a)