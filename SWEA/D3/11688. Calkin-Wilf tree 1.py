T = int(input())
for test_case in range(1, T + 1):
    orders = input()

    a, b = 1, 1
    for order in orders:
        if order == 'L':
            a, b = a, a + b

        elif order == 'R':
            a, b = a + b, b

    print(f'#{test_case} {a} {b}')
