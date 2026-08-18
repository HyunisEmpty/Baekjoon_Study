import heapq

def solution(scovilles, K):
    answer = 0
    
    # 최소힙을 활용하여 스코빌 지수의 최소값이 K 이상이 될때 까지 반복
    # 더이상 반복할 수 없을때 스코빌 지수의 최소값이 K 미만인 경우 -1 반환
    # 반복 조건, 최소힙에 2개 이상의 원소가 있고, 스코빌 지수의 최소값이 K 미만인 경우 
    
    
    heap = []
    for scoville in scovilles: 
        heapq.heappush(heap, scoville)
        
    while len(heap) >= 2 and heap[0] < K:
        answer += 1
        scoville_1 = heapq.heappop(heap)
        scoville_2 = heapq.heappop(heap)
        
        scoville_new = scoville_1 + scoville_2 * 2
        
        heapq.heappush(heap, scoville_new)
        
    if heap[0] < K:
        return -1

    return answer
