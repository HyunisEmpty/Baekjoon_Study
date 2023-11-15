import sys

n = int(sys.stdin.readline().strip())

for test in range(n):

    words = sys.stdin.readline().strip()

    left = 0
    right = len(words) - 1
    answer = 0

    while left < right:     # 문자열의 길이가 홀수이든 짝수이든 상관없는 종료 조건인다.

        if words[left] == words[right]:
            left += 1
            right -= 1
        else:   # 회문이 아닌 경우
            answer = 2

            if left == 0:
                left_words = words[left + 1:]
            else:
                left_words = words[:left] + words[left + 1:]

            if right == len(words) - 1:
                right_words = words[:right]
            else:
                right_words = words[:right] + words[right + 1:]

            if left_words[::] == left_words[::-1]:
                answer = 1
                break

            if right_words[::] == right_words[::-1]:
                answer = 1
                break
            break
    print(answer)