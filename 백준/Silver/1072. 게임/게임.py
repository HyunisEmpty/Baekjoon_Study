import sys

x, y = map(int, sys.stdin.readline().split())
z = int((y * 100) // x)

left = 0
right = sys.maxsize # 정수 최댓값
if z == 99 or z == 100:
     print(-1)
else:
     while left <= right:

           mid = (left + right)//2

           # F(mid) True인 경우
           if int(((y + mid) * 100 // (x + mid))) != z:
               answer = mid 
               right = mid - 1
           # F(mid) False인 경우
           else:
               left = mid + 1

     print(answer)



