import sys

n = int(sys.stdin.readline().strip())

for count in range(n):

    word_a, word_b = map(str, sys.stdin.readline().split())

    case_a = sorted(word_a)
    case_b = sorted(word_b)

    case_a = "".join(case_a)
    case_b = "".join(case_b)

    if case_a == case_b:
        print(word_a + " & " + word_b + " are anagrams.")
    else:
        print(word_a + " & " + word_b + " are NOT anagrams.")

