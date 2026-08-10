def solution(clothes):
    answer = 1
    clothes_dict = dict()
    
    for name, type in clothes:
        
        if type not in clothes_dict:
            clothes_dict[type] = 2
        else:
            clothes_dict[type] += 1
        
    for value in clothes_dict.values():
        answer *= value
    
    return answer - 1