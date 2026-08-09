def solution(participants, completions):
    answer = ''
    
    # 선수 명단 저장하는  딕셔너리
    participant_dict = dict()
    
    for participant in participants:
        
        if participant not in participant_dict: # 사전에 선수가 없다면
            participant_dict[participant] = 1
        else:                                   # 사전에 선수가 있다면
            participant_dict[participant] += 1
    
    for completion in completions:
        participant_dict[completion] -= 1
        
    for participant in participant_dict: 
        if participant_dict[participant] != 0:
            answer = participant
    
    return answer