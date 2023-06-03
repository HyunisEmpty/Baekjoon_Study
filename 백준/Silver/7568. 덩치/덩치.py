import sys

n = int(sys.stdin.readline().strip())
people_list = []
rank_list = []

for i in range(n):
     rank = 1
     weight, height = map(int, sys.stdin.readline().split())

     people_list.append((weight, height, rank))

for i in range(n):

    weight, height, rank = people_list[i]

    for j in range(n):

        # 자기 스스로를 비교하지 않는다.
        if i != j:
            n_weight, n_height, n_rank = people_list[j]

            # 자기 보다 덩치가 작지 않은 경우 rank 증가
            if n_weight > weight and n_height > height:
                rank += 1

    rank_list.append(str(rank))

print(" ".join(rank_list))