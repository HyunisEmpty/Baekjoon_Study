import sys

word = sys.stdin.readline().strip()

for i in range(1, len(word)//10 + 1):
    print(word[i*10-10:i*10])

print(word[(len(word)//10)*10:])