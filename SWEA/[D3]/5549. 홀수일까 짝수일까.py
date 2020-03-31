T = int(input())
for t in range(1, 1 + T):
    number = int(input())
    result = ''
    if number % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'

    print('#{} {}'.format(t, result))
