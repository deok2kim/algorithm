T = int(input())
for t in range(1, 1 + T):
    n = int(input())
    farm = [list(map(int, list(input()))) for _ in range(n)]
    #
    # for i in farm:
    #     print(i)

    left = n // 2
    right = n // 2 + 1
    # print(left, right)
    tot = 0
    for i in range(n):
        if i >= n // 2:
            tot += sum(farm[i][left:right])
            left += 1
            right -= 1
        else:
            tot += sum(farm[i][left:right])
            left -= 1
            right += 1

    print('#{} {}'.format(t, tot))

