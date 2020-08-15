T = int(input())

for t in range(1, T + 1):
    n = int(input())
    card = input().split()

    len_card = (len(card) + 1) // 2
    a = card[:len_card]
    b = card[len_card:]

    print('#{}'.format(t), end='')
    for i in range(len(a)):
        print(' ', end='')
        print(a[i], end='')
        print(' ', end='')
        if i < len(b):
            print(b[i], end='')
    print()
