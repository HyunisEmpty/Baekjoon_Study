import sys

"""
n : 알파벳 종류의 최대 개수  
m_str : 문자열
m_dict : 부분 배열의 단어의 개수를 저장
m_set : 부분 배열에 들어있는 단어의 종류를 저장
start : 부분 배열의 앞을 가르키는 인덱스 
end : 부분 배열의 뒤를 가르키는 인덱스
max_len : 번역기가 인식할 수 있는 최대길이
"""

n = int(sys.stdin.readline().strip())
m_str = sys.stdin.readline().strip()
m_dict = dict()
m_set = set()


# m_str에 대한 투 포인터 알고리즘
start = 0
end = 0
max_len = 0
while start <= end and end < len(m_str):

    word = m_str[end]

    # 해당 단어가 이미 집합에 포함된 경우
    if word in m_set:

        # 부분 배열의 문자 개수를 저장
        if word not in m_dict.keys():
            m_dict[word] = 1
        else:
            m_dict[word] += 1

        max_len = max(max_len, end - start + 1)

        end += 1

    # 해당 단어가 집합에 포합되지 않은 경우
    else:

        # 새로운 종류의 단어를 부분 배열에 포함 시켜도 되는 경우
        if len(m_set) + 1 <= n:

            # 집합에 단어 추가
            m_set.add(word)

            # 부분 배열의 문자 개수를 저장
            if word not in m_dict.keys():
                m_dict[word] = 1
            else:
                m_dict[word] += 1

            max_len = max(max_len, end - start + 1)

            end += 1

        # 새로운 종류의 단어를 부분 배열에 포함 시키면 안되는 경우, start에 있는 값을 부분 배열에서 제거
        else:

            m_dict[m_str[start]] -= 1

            if m_dict[m_str[start]] == 0 and m_str[start] in m_set:
                m_set.remove(m_str[start])

            start += 1



print(max_len)
