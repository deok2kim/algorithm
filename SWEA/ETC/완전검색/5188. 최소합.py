def recur(i, j, cur_sum):
    global min_sum
    if i == n or j == n:
        if j == n - 1:
            min_sum = min(min_sum, cur_sum)

        elif i == n - 1:
            min_sum = min(min_sum, cur_sum)

        return

    if cur_sum > min_sum:
        return

    recur(i + 1, j, cur_sum + pan[i][j])
    recur(i, j + 1, cur_sum + pan[i][j])


for tc in range(int(input())):
    n = int(input())
    pan = [list(map(int, input().split())) for _ in range(n)]

    min_sum = 9876543210
    recur(0, 0, 0)

    print('#{} {}'.format(tc+1, min_sum))
