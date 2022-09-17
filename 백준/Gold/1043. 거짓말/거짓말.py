import sys

"""입력값 정의"""
# 사람의 수와 파티의 수
person, party = map(int, sys.stdin.readline().split())
# 진실을 아는 사람
true_person_list = list(map(int, sys.stdin.readline().split()))
del true_person_list[0]
# 파티별 참석하는 사람
party_list = []
for count in range(party):
    party_list.append(list(map(int, sys.stdin.readline().split())))
    del party_list[count][0]

# print(true_person_list)
# print(party_list)

"""코드 구현"""
while len(true_person_list) != 0:
    # 현재 진실을 아는 사람
    target = true_person_list[0]
    # 제거할 2중 리스트 인덱스
    delete_party = []
    # 새로 진실을 듣게된 사람 리스트
    new_true_person_list = []

    for count_y in range(len(party_list)):
        for count_x in range(len(party_list[count_y])):

            # 만약 파티에 진실을 아는 사람이 있다면
            if party_list[count_y][count_x] == target:
                delete_party.append(count_y)

                for count_xx in range(len(party_list[count_y])):
                    # delete_party 에 새로 추가된 리스트의 원소중 타깃과 다른값이면 리스트에 저장
                    if party_list[count_y][count_xx] in true_person_list:
                        pass
                    else:
                        true_person_list.append(party_list[count_y][count_xx])

    # 현재의 타깃을 제거
    del true_person_list[0]

    delete_party.reverse()

    for count in delete_party:
        del party_list[count]

print(len(party_list))