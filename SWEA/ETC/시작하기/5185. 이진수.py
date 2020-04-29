T = int(input())
for tc in range(T):
    n, hex_numbers = input().split()

    result = ''
    for hex_number in hex_numbers:
        number = int(hex_number, 16)  # 16진수를 10진수로 변환
        # print('10진수 : ', number)
        binary_number = format(number, 'b')  # 10진수를 2진수(binary)로 변환
        # print('2진수 : ', binary_number)

        for i in range(4-len(binary_number)): # 4자리수로 맞춰주기
            result += '0'
        result += binary_number

    print('#{} {}'.format(tc+1, result))
