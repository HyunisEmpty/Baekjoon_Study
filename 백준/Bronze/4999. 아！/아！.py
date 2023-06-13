import sys

max_input = sys.stdin.readline().strip()
n_input = sys.stdin.readline().strip()

if len(max_input) >= len(n_input):
    print("go")
else:
    print("no")