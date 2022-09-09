import sys

size_count = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
change_count = int(sys.stdin.readline())

# 중간 연산을 위해 필요한 리스트
copy_array = []

# 최종출력할 리스트
last_array = []

while change_count > 0 and len(array) != 0:

    # a에는 몫을 b에는 나머지를 저장한다.
    a = change_count // len(array)
    b = change_count % len(array)

    # 만약 a가 0보다 크다면 array 전체에 접근가능하다는 것을 의미한다.
    if a > 0:
        copy_array = array[:]
    # 만약 a가 0과 같고 b가존재 한다면 array의 인덱스 b까지 접근 가능함을 의미한다.
    else:
        copy_array = array[0:b+1]
    # print("copy된 array :",copy_array)

    # copy_array중 가장 큰값을 찾는다.
    array_max = 0
    for count in copy_array:
        if count > array_max:
            array_max = count
    # print("최댓값 :", array_max)

    # 범위내 최댓값의 인덱스값을 가지고 온다.
    max_index = copy_array.index(array_max)

    # 삭제될 값을 저장한다.
    remove_target = array[max_index]
    # print("제거대상 :",remove_target)

    # 삭제될 값을 최종 출력할 리스트에 저장한다.
    last_array.append(remove_target)

    # 인덱스 값을 통해 그값을 삭제하고 change_count에서 index만큼 뺀다.
    del array[max_index]
    change_count = change_count - max_index

last_array = last_array + array
print(*last_array)


