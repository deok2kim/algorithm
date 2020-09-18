from collections import deque


def solution(s):
    answer = 1
    n = len(s)
    if n % 2 == 1:
        return 0

    q = deque()
    for word in s:
        if q:
            if q[-1] == word:
                q.pop()
            else:
                q.append(word)
        else:
            q.append(word)

    if q:
        answer -= 1

    return answer


print(solution('baabaa'))
