def solution(s):
    stack = []
    
    for word in s:
        
        stack.append(word)
        
        if len(stack) >= 2 and stack[-2] == "(" and stack[-1] == ")":
            stack.pop()
            stack.pop()
                
    if len(stack) == 0:
        return True
    else:
        return False 
            