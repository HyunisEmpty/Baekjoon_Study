from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    cnt = 1
    
    # 한번의 반복에서 하나의 값을 꺼내서 연산을 수행
    while True: 
        
        target = queue.popleft()
        location -= 1
        
        if len(queue) == 0:
            queue_max = 1
        else:
            queue_max = max(queue)
        
        # 현재 실행되야 하는 우선순위라면
        if target >= queue_max:
            if location == -1:
                return cnt
            cnt += 1
        else: 
            queue.append(target)
            if location == -1:
                location = len(queue) - 1