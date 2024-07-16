import sys

# 입력되는 수의 개수, 목표 수열, 오름차순 수열, 스택, 최종 수열
n = int(sys.stdin.readline().strip())
answer_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
start_stack = [i for i in range(1, n+1)]
stack = []
end_list = []
command_list = []
index = 0

# 최종적으로 만든 리스트에 모든 원소가 들어가면 무한반복 종료
while len(end_list) != n:

    # 스택이 비어있다면, start_stack 첫번째 값을 push
    if len(stack) == 0:

        # push 명령어, end 리스트가 최대 길이가 아니고 스택이 비어있는 경우 아직 start stack에는 값이 있다.
        stack.append(start_stack[0])
        start_stack.pop(0)
        command_list.append("push")

    # 스택이 비어있지 않다면, stack 마지막 값에 따라서 push 혹은 pop을 수행
    else:

        # push를 수행하는 경우, 스택의 마지막 값이 오면 안되는 경우
        if stack[len(stack)-1] != answer_list[index]:

            # push 명령어 수행, start stack에 가장 앞에 있는 값을 stack push
            if len(start_stack) != 0:
                stack.append(start_stack[0])
                start_stack.pop(0)
                command_list.append("push")
            # push 명령어 수행, start stack이 비어 있어 answer list를 만드는 것이 불가능한 경우
            else:

                # 명령어 삭제
                command_list.clear()
                break

        # pop을 수행하는 경우, 스택의 마지막 값이 현재 와야 하는 값인 경우
        else:

            # pop 명령어 수행
            end_list.append(stack[len(stack)-1])
            stack.pop(len(stack)-1)
            command_list.append("pop")

            # 다음 값을 확인
            index += 1
            
            
if command_list == []:
    print("NO")
else:
    for command in command_list:
        if command == "push":
            print("+")
        else:
            print("-")