from collections import deque

def solution(prices):
    answer = [0 for i in range(len(prices))]
    
    time = 1
    prices = deque(prices)
    stack = []
    stack.append((prices.popleft(), time))
    
    while prices: 
        time += 1
        price = prices.popleft()
        
        while stack and stack[-1][0] > price:
            b_price, b_time = stack.pop()
            answer[b_time - 1] = time - b_time
        
        stack.append((price, time))
    
    while stack:
        b_price, b_time = stack.pop()
        answer[b_time - 1] = time - b_time
    
    return answer