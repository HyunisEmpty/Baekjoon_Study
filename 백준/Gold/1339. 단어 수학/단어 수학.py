import sys

n = int(sys.stdin.readline().strip())
alpha_dict = dict()

for i in range(n):
    word = sys.stdin.readline().strip()
    for j in range(len(word)):
        alpha = word[j]

        if alpha not in alpha_dict:
            alpha_dict[alpha] = pow(10, (len(word) - (j + 1)))
        else:
            alpha_dict[alpha] += pow(10, (len(word) - (j + 1)))

n_list = []
for key in alpha_dict:
    n_list.append(alpha_dict[key])
n_list.sort(reverse=True)

cnt = 9
answer = 0
for i in range(len(n_list)):
    answer += n_list[i] * cnt
    cnt -= 1

print(answer)