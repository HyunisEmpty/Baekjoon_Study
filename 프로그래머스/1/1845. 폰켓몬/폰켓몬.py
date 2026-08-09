def solution(nums):
    answer = 0
    
    pm_cnt = len(nums)
    
    pm_type_cnt = len(set(nums))
    
    if pm_cnt/2 <= pm_type_cnt:
        answer = pm_cnt/2
    else:
        answer = pm_type_cnt
    
    return answer