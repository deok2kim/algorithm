def isRight(paren):
    q = []
    for p in paren:
        if p == '(':
            q.append(p)
        else:
            if q:
                q.pop()
            else:
                return False


    return True


def sep(paren):
    l = 0
    r = 0
    for i in range(len(paren)):
        if paren[i] == '(':
            l += 1
        else:
            r += 1

        if l == r:
            return paren[:i + 1], paren[i + 1:]


def solution(p):
    if p == '' or isRight(p):
        return p
    else:
        u, v = sep(p)

    if isRight(u):
        return u + solution(v)

    else:
        word = '('
        word += solution(v)
        word += ')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                word += ')'
            else:
                word += '('
    return word
