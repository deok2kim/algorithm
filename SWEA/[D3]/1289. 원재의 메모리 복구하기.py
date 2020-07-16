T = int(input())
for tc in range(1, T+1):
    init = list(input())
    n = ['0']*len(init)
    cnt = 0
    for i in range(len(n)):
        if n[i] != init[i]:
            n[i:] = init[i]*len(n[i:])
            cnt += 1

    print('#{} {}'.format(tc, cnt))
