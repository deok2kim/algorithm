for tc in range(1, 1+int(input())):
    n = int(input())
    numbers = set()
    cnt = 1
    answer = 0
    while True:
        a = list(str(n*cnt))
        for i in a:
            numbers.add(i)

        # print(n*cnt, numbers)
        if len(numbers) == 10:
            answer = n*cnt
            break
        else:
            cnt += 1

    print('#{} {}'.format(tc, answer))

    a = b
    a+=1
