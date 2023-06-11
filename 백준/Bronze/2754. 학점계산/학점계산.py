import sys

n = sys.stdin.readline().strip()

if n == "A+":
    print(4.3)
elif n == "A0":
    print(4.0)
elif n == "A-":
    print(3.7)
elif n == "B+":
    print(3.3)
elif n == "B0":
    print(3.0)
elif n == "B-":
    print(2.7)
elif n == "C+":
    print(2.3)
elif n == "C0":
    print(2.0)
elif n == "C-":
    print(1.7)
elif n == "D+":
    print(1.3)
elif n == "D0":
    print(1.0)
elif n == "D-":
    print(0.7)
else:
    print(0.0)
