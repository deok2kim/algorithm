for tc in range(int(input())):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B + 1):
        C = i ** (1 / 2)
        if C == int(C):  # 제곱근이 정수일 때
            i = str(i)
            C = str(int(C))
            if i == i[::-1] and C == C[::-1]:
                cnt += 1

    print(f'#{tc + 1} {cnt}')
