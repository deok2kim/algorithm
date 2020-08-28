def is_right(p):
    tmp = []
    for idx, paren in enumerate(p):
        if paren == '(':
            tmp.append(paren)
        else:
            if tmp:
                tmp.pop()
            else:
                return False

    if tmp:
        return False

    return True


def is_balanced(p):
    check = 0
    for idx, paren in enumerate(p):
        if paren == '(':
            check += 1
        else:
            check -= 1

        if check == 0:
            return idx


def solution(p):
    if p == '' or is_right(p):
        return p

    else:
        idx = is_balanced(p)
        u = p[:idx + 1]
        v = p[idx + 1:]

    if is_right(u):
        return u + solution(v)

    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'

        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                tmp += ')'
            else:
                tmp += '('

    return tmp


print(solution("()))((()"))
print(solution("(()())()"))
print(solution(")("))
