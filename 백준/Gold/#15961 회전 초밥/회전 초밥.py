import sys

# n : 벨트에 놓인 접시의 수, d : 초밥의 가짓수, k : 연속해서 먹는 접시의 수, c : 쿠폰 번호
n, d, k, c = map(int, sys.stdin.readline().split())
# n_list 변수에 n개의 접시위의 초밥을 입력받음, 입력값은 초밥의 종류
n_list = []
# n_set 연속해서 존재하는 접시에 있는 초밥의 종류를 저장하는 집합
n_set = set()
n_set.add(c)
# n_dict 연속해서 존재하는 접시위에 존재하는 각각의 초밥의 종류의 개수를 저장하는 딕셔너리, 키 : 초밥의 종류, 값 : 초밥의 개수
n_dict = dict()
# 두 포인터 start : 부분배열의 시작, end 부분배열의 끝
start = 0
end = k - 1
# 부분배열에 들어있는 초밥 종류의 최대 개수
max_len = 0

for i in range(n):
    n_list.append(int(sys.stdin.readline().strip()))

for i in range(k):
    if i != k - 1:
        n_list.append(n_list[i])
    # n_set 초기값 설정
    n_set.add(n_list[i])
    if n_list[i] in n_dict:
        n_dict[n_list[i]] += 1
    else:
        n_dict[n_list[i]] = 1

while end != len(n_list):

    if len(n_set) > max_len:
        max_len = len(n_set)

    # 집합에서 start가 가리키는 원소를 제거하는 연산
    # 현재 값이 쿠폰이 아니며, 부분배열에 초밥이 한개만 들어 있는 경우.
    if n_list[start] != c and n_dict[n_list[start]] == 1:
        n_set.remove(n_list[start])
    n_dict[n_list[start]] -= 1
    start += 1

    end += 1
    if end != len(n_list):
        n_set.add(n_list[end])
        if n_list[end] in n_dict:
            n_dict[n_list[end]] += 1
        else:
            n_dict[n_list[end]] = 1

print(max_len)