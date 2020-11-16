def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            new_s = s[i:j + 1]
            print(new_s)

            tmp = 0
            for k in range(len(new_s)):
                for m in range(len(new_s) - 1, -1, -1):
                    if m - k < tmp:
                        break
                    if new_s[k] != new_s[m]:
                        tmp = max(tmp, m - k)
            print(tmp)
            answer += tmp

    return answer


print(solution("baby"))
