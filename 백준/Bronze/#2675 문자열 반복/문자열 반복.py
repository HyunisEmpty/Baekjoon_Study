import sys

test = int(sys.stdin.readline().strip())

for i in range(test):
    answer = ""
    n, word = map(str, sys.stdin.readline().split())

    for j in range(len(word)):
        answer += word[j] * int(n)
    print(answer)
