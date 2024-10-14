import sys

n = int(sys.stdin.readline().strip())                           # 크레인 개수
n_list = list(map(int, sys.stdin.readline().strip().split()))   # 크레인 무게 제한 리스트
n_list.sort(reverse=True)                                       # 오름차순 정렬
m = int(sys.stdin.readline().strip())                           # 박스의 개수
m_list = list(map(int, sys.stdin.readline().strip().split()))   # 박스의 무게 리스트
m_list.sort(reverse=True)                                       # 오름차순 정렬

# print(n_list)
# print(m_list)

# 만약 모든 박스를 배로 옮길 수 없다면
if n_list[0] < m_list[0]:
    print(-1)
# 모든 박스를 배로 옮길 수 있다면
else:

    cnt = 0
    for i in range(n):        # 처음 자기가 옮길 수 있는 박스의 위치를 저장, 초기값
        if n_list[i] >= m_list[-1]: # 들 수 있는 박스가 하나라도 있는 경우
            while n_list[i] < m_list[cnt]:  # 현재 무게를 들 수 없는 경우 무한 반복
                cnt += 1
            n_list[i] = cnt                 # 자신이 들 수있는 가장 무거운 무게의 위치 저장
        else:                       # 들 수 있는 박스가 없는 경우
            n_list[i] = len(m_list)

    day_cnt = 0
    carry_all_box = False
    while not carry_all_box:    # 모든 박스를 옮겼다면

        for i in range(n):  # 각 크레인에 접근

            if n_list[i] != len(m_list):            # 아직 옮길 수 있는 상자가 남아있는 경우
                if m_list[n_list[i]] != 0:          # 상자가 있는 경우
                    m_list[n_list[i]] = 0
                    n_list[i] += 1
                else:   # 현재 옮겨야 하는 상자가 이미 옮겨진 경우 => 다음에 옮겨야 할 상자를 찾고 옮김
                    while n_list[i] < len(m_list):
                        if m_list[n_list[i]] != 0:  # 상자가 있는 경우
                            m_list[n_list[i]] = 0
                            n_list[i] += 1
                            break
                        else:                       # 상자가 없는 경우
                            n_list[i] += 1

        # 모든 크레인이 할일이 끝난 경우
        if 0 == sum(m_list):
            carry_all_box = True

        day_cnt += 1

    print(day_cnt)