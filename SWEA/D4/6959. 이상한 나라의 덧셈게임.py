
for tc in range(1, 1 + int(input())):
    numbers = list(input())

    cnt = 0
    while len(numbers) > 1:
        a = int(numbers.pop())
        b = int(numbers.pop())
        c = a + b
        d = str(c)
        if len(d) > 1:
            numbers.append(int(d[0]))
            numbers.append(int(d[1]))
        else:
            numbers.append(c)

        cnt += 1

    answer = ""
    if cnt % 2:
        answer = 'A'
    else:
        answer = 'B'

    print('#{} {}'.format(tc, answer))

