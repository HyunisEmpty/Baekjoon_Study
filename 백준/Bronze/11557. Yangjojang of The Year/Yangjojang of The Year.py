import sys

test_case = int(sys.stdin.readline().strip())

for test in range(test_case):

    college_number = int(sys.stdin.readline().strip())
    max_college = ["test", "test"]

    for count in range(college_number):
        test_college = list(map(str, sys.stdin.readline().split()))
        if count == 0:
            max_college[0] = test_college[0]
            max_college[1] = test_college[1]
        else:
            if int(test_college[1]) > int(max_college[1]):
                max_college[0] = test_college[0]
                max_college[1] = test_college[1]
    print(max_college[0])
