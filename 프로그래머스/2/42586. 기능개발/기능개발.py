# Queue로 해결 가능 -> progresses의 왼쪽에서 pop에서 진도율이 100% 이상인 경우에만 배포가 이루어지기 때문이다. 
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)  
    speeds = deque(speeds)
    
    while len(progresses) != 0:
        # 오늘 하루 배포된 기능의 수를 저장
        cnt = 0     
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        while len(progresses) != 0 and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
            
        if cnt != 0:
            answer.append(cnt)
    
    return answer