def solution(s):
    answer = float('inf')
    if len(s) == 1:
        return 1
    n = len(s)
    results = []
    for i in range(1, n // 2 + 1):
        tmp = []
        for j in range(0, n, i):
            tmp.append(s[j:j + i])
        results.append(tmp)

    for result in results:
        cnt = 1
        word = ''
        for j in range(len(result) - 1):

            if result[j] == result[j + 1]:
                cnt += 1
            else:
                if cnt > 1:
                    word += f'{cnt}{result[j]}'
                else:
                    word += f'{result[j]}'

                cnt = 1
        else:
            if cnt > 1:
                word += f'{cnt}{result[j]}'
            else:
                word += f'{result[j + 1]}'
        answer = min(answer, len(word))

    return answer


print(solution('abab'))
print(solution('ababc'))
print(solution('ababca'))
print(solution('abaaba'))
print(solution('a'))
