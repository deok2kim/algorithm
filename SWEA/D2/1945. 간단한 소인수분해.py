T = int(input())
for tc in range(1, T + 1):
    numbers = [2, 3, 5, 7, 11]
    result = []
    n = int(input())
    idx = 0
    for number in numbers:
        cnt = 0
        while True:
            if n % number == 0:
                n = n // number
                cnt += 1

            else:
                result.append(str(cnt))
                break

    print('#{} {}'.format(tc, ' '.join(result)))
