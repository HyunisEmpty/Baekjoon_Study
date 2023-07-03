import sys

people, width = map(int, sys.stdin.readline().split())
article = list(map(int, sys.stdin.readline().split()))
new_article = []
n = people * width
               
for target in article:
    new_article.append(target - n)

answer = ""
for target in new_article:
    answer += str(target) + " "
print(answer)
