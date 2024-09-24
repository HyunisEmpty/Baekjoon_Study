import sys

n_str = list(sys.stdin.readline().strip())
n_target = list(sys.stdin.readline().strip())

n_stack = list()

for n in n_str:
    n_stack.append(n)

    # 스택안에 문자열이 폭발 문자열보다 길거나 같은 경우
    if len(n_stack) >= len(n_target):

        # 뒤의 문자열이 폭발 문자열인지 확인
        if n_stack[-1 * len(n_target):] == n_target:

            # 폭발 문자열 제거
            for i in range(len(n_target)):
                n_stack.pop()

if "".join(n_stack) == "":
    print("FRULA")
else:
    print("".join(n_stack))