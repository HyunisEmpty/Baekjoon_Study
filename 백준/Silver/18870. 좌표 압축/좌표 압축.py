import sys

n = int(sys.stdin.readline().strip())

number_list = list(map(int, sys.stdin.readline().split()))

# 중복 제거 및 정렬 
sort_number_list = list(set(number_list))
sort_number_list.sort()

# 각 value의 순서를 dictional에 키와 값으로 저장한다. 좌표의 값이 키로 좌표의 순서가 값으로 간다.
index_dic = {}
counter = 0
for number in sort_number_list:
    index_dic[number] = counter
    counter += 1

index_list = []
for number in number_list:
    index_list.append(str(index_dic[number]))

print(" ".join(index_list))

"""
index_list = []
for number in number_list:
    index_list.append(str(sort_number_list.index(number)))
print(" ".join(index_list))
다음 코드는 index를 통해서 좌표 압축을 하려했던 코드이다. index의 경우 시간 복잡도가 O(n)이다. 
그런데 이를 n개의 원소에 반복함으로 시간복잡도가 O(n^2)가 되기 때문에 index()를 사용할 수 없다. 
그렇기에 나는 시간복잡도가 O(1)인 딕셔너리를 이용했다. 
"""
 
