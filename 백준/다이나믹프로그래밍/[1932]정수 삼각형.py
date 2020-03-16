import sys

N = int(sys.stdin.readline())
pyramid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for i in range(N-1, -1, -1):
    for j in range(i):
        pyramid[i-1][j] += max(pyramid[i][j], pyramid[i][j+1])

print(pyramid[0][0])
