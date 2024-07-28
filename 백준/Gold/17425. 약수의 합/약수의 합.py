import sys

"""
변수 저장 
tc : 테스트 케이스 개수
tc_list : 테스트 케이스 리스트
max_tc : 테스트 케이스 최댓값 
f_list : 1부터 max_tc까지의 f(x) 리스트
g_list : f(x)리스트의 누적합을 저장
"""

tc = int(sys.stdin.readline().strip())
tc_list = []


# 테스트 케이스 입력
max_tc = 0
for i in range(tc):
    tc_list.append(int(sys.stdin.readline().strip()))
max_tc = max(tc_list)

# f_list의 0빼고 모든 수에 접근(인덱스가 값을 의미)
f_list = [0] * (max_tc + 1)
for i in range(1, max_tc + 1):

    measure = i
    cnt = 1

    while measure * cnt <= max_tc:
        f_list[measure * cnt] += measure
        cnt += 1

# g_list에 f_list 누적합 저장
g_list = [0] * (max_tc + 1)
for i in range(1, max_tc + 1):
    g_list[i] = f_list[i] + g_list[i - 1]

# 테스트 케이스 출력
for i in range(tc):
    print(g_list[tc_list[i]])