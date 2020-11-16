def solution(n):
    answer = 0

    # 3진법
    mok = 0
    nmg = 0
    number = ''
    while True:
        mok = n // 3
        nmg = n % 3
        number += str(nmg)
        if mok < 3:
            number += str(mok)
            break
        n = mok
    print(number)

    # 10진법으로 바꾸기
    leng = len(number)
    for i in range(leng):
        answer += 3 ** (leng - 1 - i) * int(number[i])

    return answer


print(solution(3))
