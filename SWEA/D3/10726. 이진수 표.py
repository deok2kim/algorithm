for tc in range(int(input())):
    N, number = map(int, input().split())
    bin_number = list(map(str, str(bin(number))[2:]))[-N:]
    print(f'#{tc + 1}', end=' ')
    if len(bin_number) < N:
        print('OFF')
    else:
        if '0' in bin_number:
            print('OFF')
        else:
            print('ON')
