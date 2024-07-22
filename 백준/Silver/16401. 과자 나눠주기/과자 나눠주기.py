import sys

people, cookie = map(int, sys.stdin.readline().split())
cookie_list = list(map(int, sys.stdin.readline().split()))
cookie_list.sort(reverse=True)

left = 1
right = cookie_list[0]
max_cookie = 0

while left <= right:

    mid = (left + right) // 2

    cookie_count = 0

    for now_cookie in cookie_list:
        if now_cookie//mid != 0:
            cookie_count += now_cookie//mid
        else:
            break

    if cookie_count >= people:
        max_cookie = mid
        left = mid + 1
    else:
        right = mid - 1

print(max_cookie)