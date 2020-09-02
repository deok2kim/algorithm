import math
def findK():
    cnt = 1
    for i in range(N):
        for j in range(M):
            maps[i][j] = cnt
            if cnt == K:
                return i,j
            cnt += 1
    return 0,0

if __name__ == "__main__":

    N, M, K = map(int, input().split())
    maps = [[0]*M for _ in range(N)]

    x,y = findK()
    if x == 0 and y == 0:
        x,y = N-1, M-1
        c = math.factorial(x+y)//(math.factorial(x) * math.factorial(y))
    else:
        a = math.factorial(x + y) // (math.factorial(x) * math.factorial(y))
        b = math.factorial(N-1-x + M-1-y) // (math.factorial(N-1-x) * math.factorial(M-1-y))
        c=a*b
    print(c)


