import sys
# 원소의 개수를 입력 받음
n = int(sys.stdin.readline().strip())
# 오름 차순 정렬
n_list = sorted(list(map(int, sys.stdin.readline().split())))

# 양수와 음수만을 저장하는 각각의 리스트를 오름차순과 내림차순으로 정의한다.
pos_list = [pos for pos in n_list if pos >= 0] # 오름차순
neg_list = [neg for neg in n_list[::-1] if neg < 0]   # 내림차순


# 변수 설정
abs_min = local_abs_min = 2000000000 # 최솟값이 되는 abs 저장하는 변수로 그합이 20억이 될 수 없으므로 20억으로 초기화
answer = "" # 오름차순으로 출력할 정답을 저장하는 변수
pos_index = neg_index = 0

# 리스트의 길이가 2이상일때만 리스트에서 절댓갑이 0에 가장 가까운 2개원소의 합으로 최솟값을 초기화 한다.
if len(pos_list) > 1 and len(neg_list) > 1:
    if abs(pos_list[0] + pos_list[1]) > abs(neg_list[0] + neg_list[1]):
        abs_min = abs(neg_list[0] + neg_list[1])
        answer = str(neg_list[1]) + " " + str(neg_list[0])
    else:
        abs_min = abs(pos_list[0] + pos_list[1])
        answer = str(pos_list[0]) + " " + str(pos_list[1])
# 리스트의 길이가 1이하인 리스트가 존재 하는 경우
else:
    if len(pos_list) > 1:
        abs_min = abs(pos_list[0] + pos_list[1])
        answer = str(pos_list[0]) + " " + str(pos_list[1])
    if len(neg_list) > 1:
        abs_min = abs(neg_list[0] + neg_list[1])
        answer = str(neg_list[1]) + " " + str(neg_list[0])
    # 위 두가지 연산을 하지 않는 경우는 각 리스트의 길이가 1인 경우 이다.

# 위 연산에서 그 어떤 조건문에도 실행되지 않을 경우는 두 리스트의 길이가 각각 1이 되는 경우이다.
while pos_index != len(pos_list) and len(neg_list) != 0:    # len(neg_list) != 0 neg_list의 길이가 0인 경우에도 무한 반복문이 실행되 실행문 첫번째 neg_list의 원소를 호출하는 IndexError가 발생할 수 있다.

    n_sum = abs(pos_list[pos_index] + neg_list[neg_index])

    if local_abs_min > n_sum: #초기 연산인 경우, 이전 합보다 절댓값이 작아진 경우
        local_abs_min = n_sum
        if neg_index + 1 != len(neg_list):
            neg_index += 1
    elif local_abs_min == n_sum:    # 이전 합과 절댓값이 같아진 경우, neg_index가 증가하지 않은 경우
        if abs_min > local_abs_min:
            abs_min = local_abs_min
            answer = str(neg_list[neg_index]) + " " + str(pos_list[pos_index])
        local_abs_min = 2000000000
        pos_index += 1
    else: # 이전 합보다 절댓값이 증가한 경우
        neg_index -= 1
        if abs_min > local_abs_min:
            abs_min = local_abs_min
            answer = str(neg_list[neg_index]) + " " + str(pos_list[pos_index])
        local_abs_min = 2000000000
        pos_index += 1

print(answer)