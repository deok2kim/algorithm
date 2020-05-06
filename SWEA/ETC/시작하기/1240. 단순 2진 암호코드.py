T = int(input())
for tc in range(T):
    sero, garo = map(int, input().split())
    numbers = [input() for _ in range(sero)]

    secret_code = ''
    for number in numbers:
        if '1' in number:
            secret_code = number
            break

    for i in range(garo-1, -1, -1):
        if secret_code[i] == '1':
            secret_code = secret_code[i-56+1:i+1]
            break
    # print(secret_code)

    secret_dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,

    }

    trans_secret_code = []
    for i in range(0, 56, 7):
        trans_secret_code.append(secret_dict[secret_code[i:i+7]])
    # print(trans_secret_code)

    cal = 0
    for i in range(8):
        if i % 2 == 0:
            cal += trans_secret_code[i]*3
        else:
            cal += trans_secret_code[i]
    # print(cal)

    result = 0
    if cal % 10 == 0:
        result = sum(trans_secret_code)

    print('#{} {}'.format(tc+1, result))
