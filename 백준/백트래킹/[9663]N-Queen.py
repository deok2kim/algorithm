# 파이썬으로 제출 시 시간초과
def check(x, y):
    for k in range(3):
        nx = x
        ny = y
        while True:
            nx += dx[k]
            ny += dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if chess[nx][ny] == 1:
                    return False
            else:
                break

    return True


def backtracking(idx=0):
    # for i in chess:
    #     print(i)
    # print()
    global result
    if idx == n:
        result += 1
        # for i in chess:
        #     print(i)
        # print()
        return

    for i in range(n):
        if chess[idx][i] == 0 and check(idx, i):
            chess[idx][i] = 1
            backtracking(idx+1)
            chess[idx][i] = 0
    return


n = int(input())

chess = [[0]*n for _ in range(n)]
dx = [-1, -1, -1]
dy = [-1, 0, 1]

result = 0
backtracking()
print(result)
