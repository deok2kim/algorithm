lst = []
T = int(input())
for tc in range(T):
    lst.append(tuple(map(int, input().split())))

for tc in range(T):
    A, B, C, D = lst[tc]
    ALICE = A / B
    BOB = C / D
    print(f'#{tc + 1}', end=' ')
    if ALICE > BOB:
        print('ALICE')
    elif ALICE < BOB:
        print('BOB')
    else:
        print('DRAW')
