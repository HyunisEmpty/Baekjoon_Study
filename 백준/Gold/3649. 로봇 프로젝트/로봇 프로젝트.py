import sys

while True:

    x = sys.stdin.readline().strip()

    if x == "":
        break
    
    x = int(x) * 10000000
    n = int(sys.stdin.readline().strip())
    n_list = []
    answer = "danger"
    start = 0
    end = n - 1

    for i in range(n):
        n_list.append(int(sys.stdin.readline().strip()))
    n_list.sort()

    while start < end:

        val_sum = n_list[start] + n_list[end]

        if val_sum == x:
            answer = "yes " + str(n_list[start]) + " " + str(n_list[end])
            break
        elif val_sum > x:
            end -= 1
        elif val_sum < x:
            start += 1

    print(answer)