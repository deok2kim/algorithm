def solution(n, words):
    answer = []
    len_words = len(words)
    wrong = 0
    for i in range(1, len_words):
        if words[i - 1][-1] != words[i][0] or words[i] in words[:i]:
            wrong = i + 1
            break
    # print(wrong, n)
    if wrong == 0:
        answer = [0, 0]

    elif wrong % n == 0:
        answer = [n, wrong // n]

    else:
        answer = [wrong % n, wrong // n + 1]
    return answer


print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5,
               ['hello', 'observe', 'effect', 'take', 'either', 'recognize',
                'encourage', 'ensure', 'establish', 'hang',
                'gather', 'refer', 'reference', 'estimate', 'executive']))
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))

print(solution(2, ['qwq', 'qqq', 'qrq', 'qqq']))
print(solution(2, ['qwq', 'qwq']))  # 같은 턴에 중복 오류
print(solution(2, ['qwe', 'eqwe', 'eqwe']))
print(solution(2, ['land', 'dream', 'mom', 'rom', 'mom']))
print(solution(2, ['qwe', 'eqwe', 'eqwe']))
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "bot", "tank"]))
