from _collections import deque


def solution(s):
    answer = 1
    s = list(s)
    stack = []
    idx = 0
    while idx != len(s):
        stack.append(s[idx])
        idx += 1
        if len(stack) >= 2:
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()

    if not stack:
        answer = 1
    else:
        answer = 0

    return answer


print(solution('baabaa'))
print(solution('cdcd'))
