from _collections import deque

test_case = int(input())
for test_count in range(test_case):

    #변수 define
    last_list = deque() #최종출력될 문자들이 저장되는 리스트
    index_count = 0 #커서가 가리키는 방향

    #값을 입력받고 리스트화 한다.
    string_case = input()
    string_list = list(string_case)

    for input_data in string_list:

        if input_data == ">": #오른쪽으로 한칸 이동
            if index_count == len(last_list) :
                pass
            else:
                index_count += 1

        elif input_data == "<": #왼쪽으로 한칸 이동
            if index_count == 0:
                pass
            else:
                index_count -= 1

        elif input_data == "-": #현재 커서가 가리키는 곳 앞에있는값 제거
            if index_count == 0:
                pass
            else:
                del last_list[index_count - 1]
                index_count -= 1


        else: #그외를 모든 입력값
            last_list.insert(index_count, input_data)
            index_count += 1

    last_string = ""

    for input_data in last_list:
        last_string = last_string + input_data
    print(str(last_string))
