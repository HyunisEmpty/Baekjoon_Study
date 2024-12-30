import sys

angle_list = []

for _ in range(3):
    angle_list.append(int(sys.stdin.readline().strip()))

if sum(angle_list) == 180:

    # 3각이 같은 경우
    if angle_list[0] == angle_list[1] and angle_list[1] == angle_list[2]:
        print("Equilateral")
    # 같은 각이 없는 경우
    elif angle_list[0] != angle_list[1] and angle_list[1] != angle_list[2] and angle_list[0] != angle_list[2]:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")