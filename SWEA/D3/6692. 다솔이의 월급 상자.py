for tc in range(int(input())):
    N = int(input())

    avg = 0
    for _ in range(N):
        tmp = input().split()
        p = float(tmp[0])
        x = int(tmp[1])
        avg += p * x

    # print(f'#{tc + 1} {total:6f}')
    print(f'#{tc + 1} {avg:.6f}')
