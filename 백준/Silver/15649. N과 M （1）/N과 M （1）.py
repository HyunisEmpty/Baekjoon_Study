import sys

n, m = map(int, sys.stdin.readline().split())

# 수열을 만드는 함수에게 가장 필요한 것은? 어떤 수가 있는지,
def NP(used, sequence):

    if len(sequence) == m:
        return print(" ".join(map(str, sequence)))
    else:

        for number in range(1, n + 1):
            if number not in used:
                NP(used | {number}, sequence + [number])

NP(set(), [])