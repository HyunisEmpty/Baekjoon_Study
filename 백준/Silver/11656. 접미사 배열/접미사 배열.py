import sys

word = sys.stdin.readline().strip()
word_list = []

for index in range(len(word)):
    word_list.append(word[index:])

word_list.sort()

for i in word_list:
    print(i)