# T = int(input())
# for t in range(1, 1 + T):
#     n = int(input())
#     farm = [list(map(int, list(input()))) for _ in range(n)]
#     #
#     # for i in farm:
#     #     print(i)
#
#     left = n // 2
#     right = n // 2 + 1
#     # print(left, right)
#     tot = 0
#     for i in range(n):
#         if i >= n // 2:
#             tot += sum(farm[i][left:right])
#             left += 1
#             right -= 1
#         else:
#             tot += sum(farm[i][left:right])
#             left -= 1
#             right += 1
#
#     print('#{} {}'.format(t, tot))
#

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, list(input().strip()))) for _ in range(N)]

    m = N // 2  # 중심
    answer = 0
    for i in range(m+1):  # 위아래가 대칭이므로 절반까지만 구한다.
        for j in range(m - i, m + i + 1):  # 중심을 기준으로 왼쪽으로 1칸, 오른쪽으로 1칸 범위를 늘려 나간다.
            answer += farm[i][j] + farm[N-i-1][j]

    print(f'#{test_case} {answer - sum(farm[m])}')  # 가운데를 두번 더해줬으므로 한번은 다시 빼준다.
