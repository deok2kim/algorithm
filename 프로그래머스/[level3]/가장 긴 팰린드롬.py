def pal(s):
    for i in range(len(s), -1, -1):
        for j in range(len(s) - i + 1):
            # print(s[j:j+i])
            word = s[j:j + i]
            revers_word = word[::-1]
            if word == revers_word:
                # print(word)
                return len(word)


def solution(s):
    answer = 0
    answer = pal(s)

    return answer


print(solution("abcdcba"))
print(solution("abacde"))
