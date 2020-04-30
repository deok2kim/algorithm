T = int(input())
for tc in range(T):
    number = float(input())
    # print(number)
    '''
    소수점 이하 10진수를 2진수로 바꾸는 방법
    0.6875 x 2 = 1.375 -> 1
    0.375 x 2 = 0.75 -> 0
    0.75 x 2 = 1.5 -> 1
    0.5 x 2 = 1 -> 1
    '''
    result = ''
    while True:
        number = number*2
        if number == 1:
            result += '1'
            break
        elif number > 1:
            result += '1'
            number -= 1
        else:
            result += '0'

        if len(result) == 13:
            result = 'overflow'
            break

    print('#{} {}'.format(tc+1, result))
    