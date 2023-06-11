import sys
aeiou_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

while True:
    count = 0
    input_string = sys.stdin.readline().strip()

    if input_string == "#":
        break
    else:
        for word in input_string:
            if word in aeiou_set:
                count += 1

    print(count)
