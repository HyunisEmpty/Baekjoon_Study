from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    time = 0
    bridge = deque()
    truck_weights = deque(truck_weights)
    
    print(truck_weights)
    
    while bridge or truck_weights:
        time += 1
        
        # 다리위 Truck의 무게를 1씩 증가
        for i in range(len(bridge)): 
            bridge[i][1] += 1
        
        # 현재 다리에 가장 먼저 들어있던 Truck 다리를 통과하는 경과 시간이 지났다면
        if bridge and bridge[0][1] > bridge_length:
            truck_weight, truck_time = bridge.popleft()
            weight += truck_weight
                
        # 새로운 Truck이 다리에 들어올 수 있다면 추가
        if truck_weights and weight - truck_weights[0] >= 0:
            truck_weight = truck_weights.popleft()
            bridge.append([truck_weight, 1])
            weight -= truck_weight
    
    return time