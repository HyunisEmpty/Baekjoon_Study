import sys

word_list = [
"Never gonna give you up"
,"Never gonna let you down"
,"Never gonna run around and desert you"
,"Never gonna make you cry"
,"Never gonna say goodbye"
,"Never gonna tell a lie and hurt you"
,"Never gonna stop"
]

word_list = set(word_list)
flag = True
n = int(sys.stdin.readline().strip())

for i in range(n):
    target = sys.stdin.readline().strip()

    if target not in word_list:
        flag = False
        break

if flag:
    print("No")
else:
    print("Yes")
