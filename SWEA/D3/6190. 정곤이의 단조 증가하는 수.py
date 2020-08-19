T = int(input())
for t in range(1,T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)
    result = -1

    for i in range(n):
        for j in range(i + 1, n):
            danjo = numbers[i] * numbers[j]
            il = danjo % 10
            sip = danjo // 10
            check = True

            while sip > 0:
                if il < sip % 10:
                    check = False
                    break

                else:
                    il = sip % 10
                    sip = sip // 10

            if check is True:
                if danjo > result:
                    result = danjo

    print('#{} {}'.format(t, result))
