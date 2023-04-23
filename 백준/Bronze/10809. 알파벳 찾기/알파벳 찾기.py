import sys

word = sys.stdin.readline().strip()

alphabet_dict = {}
alphabet_list = list("abcdefghijklmnopqrstuvwxyz")

for i in range(len(alphabet_list)):
    alphabet_dict[alphabet_list[i]] = -1

for i in range(len(word)):
    if alphabet_dict[word[i]] == -1:
        alphabet_dict[word[i]] = i

print(*alphabet_dict.values())