import sys

word = sys.stdin.readline().strip()

if word == "M":
    print("MatKor")
if word == "W":
    print("WiCys")
if word == "C":
    print("CyKor")
if word == "A":
    print("AlKor")
if word == "$":
    print("$clear")