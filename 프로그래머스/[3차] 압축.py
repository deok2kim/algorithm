def solution(msg):
    lzw_dict = {}
    for i in range(ord('A'), ord('Z') + 1):
        lzw_dict[chr(i)] = i-ord('A')+1

    answer = []
    idx = 0
    word = ''
    dict_number = 26
    len_msg = len(msg)

    while idx < len_msg:
        if idx < len_msg:
            word += msg[idx]

        if idx == len_msg-1 and lzw_dict.get(word):
            answer.append(lzw_dict[word])
            break

        if lzw_dict.get(word):
            idx += 1
            continue

        else:
            answer.append(lzw_dict[word[:-1]])
            dict_number += 1
            lzw_dict[word] = dict_number
            word = ''
    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))