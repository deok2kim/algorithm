T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for num in b:
        l = 0
        r = n-1
        check = 0

        while r >= l:
            m = (l + r) // 2

            if a[m] == num:
                cnt += 1
                break

            elif a[m] > num:
                if check == 1:
                    break
                else:
                    check = 1
                    r = m-1

            elif a[m] < num:
                if check == -1:
                    break
                else:
                    check = -1
                    l = m+1

    print('#{} {}'.format(tc+1, cnt))

