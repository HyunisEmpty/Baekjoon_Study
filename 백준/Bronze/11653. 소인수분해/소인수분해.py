import sys
number = int(sys.stdin.readline().strip())
for count in range(2,number+1):
    while(number%count == 0):
        number = number / count
        print((count))