from collections import deque

def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    # Stack 자료구조 활용
    for num in arr: 
        if answer[-1] != num: 
            answer.append(num)
    
    return answer