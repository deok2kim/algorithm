def solution(S):
    answer = 0
    a_cnt = 0
    S += 'T'
    for i in range(len(S)):
        c_word = S[i]
        if a_cnt == 3:
            return -1

        if c_word == 'a':
            a_cnt += 1
        else:
            answer += 2-a_cnt
            a_cnt = 0

    return answer

print(solution("aabab"))
print(solution("dog"))
print(solution("aa"))
print(solution("baaaa"))

"Given an array of strings, find a pair of strings that share the same letter at the same position."