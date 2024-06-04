import sys

province_count = int(sys.stdin.readline().strip())
province_list = sorted(list(map(int, sys.stdin.readline().split())))
max_budget = int(sys.stdin.readline().strip())
answer = 0

if sum(province_list) > max_budget:
     start = 1
     end = province_list[-1]

     while start <= end:

          sum_budget = 0

          mid = (start + end)//2

          for province in province_list:
               if province > mid:
                    sum_budget += mid
               else:
                    sum_budget += province

          # 현재 상한액으로 요청 예산을 계산했을때, 예산 총액보다 크다면 상한액을 더 낮춰야한다.(데이터 범위가 작은쪽으로 이동한다.)
          if sum_budget > max_budget:
               end = mid - 1
          else: # C라는 상황을 만족하느 경우이므로 현재 예산 상한액은 정답이 될 수 있다.
               start = mid + 1
               answer = mid

     print(answer)
else:
     print(province_list[-1])