import sys
from collections import deque

# house_count (2 ≤ house_count ≤ 200,000), router_count (2 ≤ router_count ≤ house_count)
house_count, router_count = map(int, sys.stdin.readline().split())
house_list = sorted([int(sys.stdin.readline().strip()) for _ in range(house_count)])

# 공유기를 C개 설치할 수 있는 경우에, 공유기 사이 거리의 최솟값.
# 공유기 사이의 거리 범위에 대해서 이분 탐색을 적용한다.

answer = 0

start = 1
end = house_list[-1] - house_list[0]

while start <= end:

     mid = (start + end)//2

     fore_house = house_list[0]
     # 첫번째 집에는 공유기가 설치된 상태로 시작한다.
     installed_router = 1


     # 공유기 C개를 설치 할 수 있는지 확인하는 반복문
     for house in house_list:

          if house - fore_house >= mid:
               installed_router += 1
               # 공유기 설치된 집이 바뀌면 최신화
               fore_house = house

     # 설치된 router가 목표값을 만족한다면
     if installed_router >= router_count:
          start = mid + 1
          answer = mid
     else:
          end = mid - 1

print(answer)