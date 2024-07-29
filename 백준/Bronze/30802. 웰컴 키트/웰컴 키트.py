import sys

n = int(sys.stdin.readline().strip())
shirt_list = list(map(int, sys.stdin.readline().strip().split()))
shirt_bundle, pencil_bundle = map(int, sys.stdin.readline().split())
shirt_bundle_answer = 0

for shirt in shirt_list:

    shirt_bundle_answer += shirt//shirt_bundle
    if shirt%shirt_bundle != 0:
        shirt_bundle_answer += 1

print(shirt_bundle_answer)
print(n//pencil_bundle, n%pencil_bundle)