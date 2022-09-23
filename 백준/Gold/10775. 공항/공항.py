import sys

gate_count = int(sys.stdin.readline().strip())
plane_count = int(sys.stdin.readline().strip())
parent_gate_list = []
answer = 0

for count in range(0, gate_count + 1):
    parent_gate_list.append(count)


def FindGate(gate_number):
    if parent_gate_list[gate_number] == gate_number:
        return gate_number
    parent_gate_list[gate_number] = FindGate(parent_gate_list[gate_number])
    return parent_gate_list[gate_number]


def UnionGate(gate_number_1, gate_number_2):
    gate_number_1 = FindGate(gate_number_1)
    gate_number_2 = FindGate(gate_number_2)
    parent_gate_list[gate_number_1] = gate_number_2


for count in range(plane_count):
    target = int(sys.stdin.readline().strip())
    doc = FindGate(target)

    if doc != 0:
        UnionGate(doc, doc-1)
        answer += 1
    else:
        break

print(answer)