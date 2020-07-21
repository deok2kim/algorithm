def dfs(cnt, tot, x, y):
    global result
    # 함수정지 조건
    if cnt == n:
        tot = tot + abs(x-company[0]) + abs(y-company[1])
        result = min(tot, result)
        return

    # 가지치기 | 중간 계산 결과라도 현재 얻은 최솟값보다 크면 어짜피 답이 될 수 없으므로 pass
    if tot > result:
        return

    # 완전탐색
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            dfs(cnt+1, tot + abs(x-customer[i*2])+abs(y-customer[i*2+1]), customer[i*2], customer[i*2+1])
            visit[i] = False

    return


for tc in range(1, 1 + int(input())):
    n = int(input())
    customer = list(map(int, input().split()))
    home = [customer.pop(0), customer.pop(0)]
    company = [customer.pop(0), customer.pop(0)]
    visit = [False]*n
    result = float('inf')
    dfs(0, 0, home[0], home[1])

    # print(customer, home, company)
    print('#{} {}'.format(tc, result))

'''
3
5
0 0 100 100 70 40 30 10 10 5 90 70 50 20
6
88 81 85 80 19 22 31 15 27 29 30 10 20 26 5 14
10
39 9 97 61 35 93 62 64 96 39 36 36 9 59 59 96 61 7 64 43 43 58 1 36
'''