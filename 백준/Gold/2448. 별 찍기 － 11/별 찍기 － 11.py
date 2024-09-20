import sys
import math

n = int(sys.stdin.readline().strip())
k = int(math.log2(n//3))

base_case = """  *  
 * * 
*****"""
base_lines = list(map(str, base_case.split('\n')))

# gap_minus = 3
# gap = n - gap_minus

for i in range(k):

    # gap_minus *= 2
    # gap -= 3 * (i + 1)

    # base_line에 값을 추가하며 발생할 수 있는 오류 방지
    base_len = len(base_lines)
    # 자기 유사성에 따른 자기 복제
    for j in range(base_len):

        # 현재 자신의 형태를 2개로 이어 붙여 아래에 추가
        base_lines.append(base_lines[j] + " " +  base_lines[j])
        # 현재 자신의 복사 형태가 들어오면서 생긴 차이만큼 공백 추가
        base_lines[j] = ( " " * base_len ) + base_lines[j] + ( " " * base_len )

    # # 자기 유사성에 따른 자기 복제후 출력, 새로 추가된 만큼 연산
for i in range(len(base_lines)):
    print(base_lines[i])




