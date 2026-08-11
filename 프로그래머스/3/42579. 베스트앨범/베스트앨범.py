def solution(genres, plays):
    answer = []
    genres_dict = dict()
    total_play_dict = dict()
    
    song_number = 0
    for genre, play in zip(genres, plays):
        if genre not in genres_dict:
            genres_dict[genre] = [(play, song_number)]
            total_play_dict[genre] = play
        else:
            genres_dict[genre].append((play, song_number))
            total_play_dict[genre] += play
        song_number += 1
        
    for genre in genres_dict:
        genres_dict[genre].sort(key=lambda x: -x[0])
        
    # print(genres_dict)
    
    total_play_list = list(total_play_dict.items())
    total_play_list.sort(key=lambda x: -x[1])
    
    # 장르별 총 재생횟수가 높은 장르 순서대로 반복탐색
    for genre, total_play in total_play_list:
        
        cnt = 0
        for play, song_number in genres_dict[genre]:
            if cnt == 2:
                break
            answer.append(song_number)
            cnt += 1
        
        
        # print(genre, total_play)
    # print(answer)
        
    return answer