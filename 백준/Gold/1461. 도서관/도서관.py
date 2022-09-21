import sys

# 책의 개수, 한번에 들고 다닐 수 있는 책의 개수
book_count, book_carry = map(int, sys.stdin.readline().split())

# 책의 위치를 리스트로 받아 온다.
book_list = list(map(int, sys.stdin.readline().split()))
# 양수값을 저장하는 리스트
book_list_1 = [0]
# 음수값 저장하는 리스트
book_list_2 = [0]

# book_list 에 있는 각데이터 들을 element 로 받아온다
for element in book_list:
    # element 가 0보다 크다면 book_list_1에 저장한다.
    if element > 0:
        book_list_1.append(element)
    # element 가 1보다 크다면 book_list_2에 저장한다.
    if element < 0:
        book_list_2.append(-1*element)

# book_list_1이랑 book_list_2를 내림차순으로 한다.
book_list_1.sort(reverse=True)
book_list_2.sort(reverse=True)

# 걸수음거리를 계산 하는 변
walk_count = 0
# 가장 멀리있는 책의 위치를 계산
if book_list_1[0] > book_list_2[0]:
    # 옮길수 있는 책의 수만큼 가장 멀리있는 책을 지우고 가서 끝내기에 끝냄
    for count in range(book_carry):
        # 가장 멀리있는 책의 위치를 더한다.
        if count == 0:
            walk_count += book_list_1[0]
        if len(book_list_1) != 0:
            del book_list_1[0]
else:
    for count in range(book_carry):
        if count == 0:
            walk_count += book_list_2[0]
        if len(book_list_2) != 0:
            del book_list_2[0]

# book_list_1 이나 book_list_2 중 하나라도 비어 있지 않으면 실행됨
while book_list_1 != [] or book_list_2 != []:

    # 옮길수 있는 양보다 책이 더 많을때
    if len(book_list_1) >= book_carry:
        for count in range(book_carry):
            if count == 0:
                walk_count += book_list_1[0] * 2
            del book_list_1[0]
    else:
        for count in range(len(book_list_1)):
            if count == 0:
                walk_count += book_list_1[0] * 2
            del book_list_1[0]

    if len(book_list_2) >= book_carry:
        for count in range(book_carry):
            if count == 0:
                walk_count += book_list_2[0] * 2
            del book_list_2[0]
    else:
        for count in range(len(book_list_2)):
            if count == 0:
                walk_count += book_list_2[0] * 2
            del book_list_2[0]

print(walk_count)