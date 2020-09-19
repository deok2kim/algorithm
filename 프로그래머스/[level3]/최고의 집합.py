def solution(n, s):
    if s % n == 0:
        mok = s // n
        answer = [mok for _ in range(n)]

    else:
        nmg = s % n
        mok = s // n
        answer = [mok for _ in range(0,n-nmg)]
        for i in range(nmg):
            answer.append(mok+1)

    if 0 in answer:
        answer = [-1]
    return answer


print(solution(2,9))
print(solution(2,1))
print(solution(2,8))