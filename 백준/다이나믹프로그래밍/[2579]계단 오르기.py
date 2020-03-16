import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]

if N > 2:

    max_score = [stairs[0], stairs[0] + stairs[1], max(stairs[2] + stairs[0], stairs[2] + stairs[1])]

    for i in range(3, N):
        max_score.append(max(stairs[i] + stairs[i - 1] + max_score[i - 3], stairs[i] + max_score[i - 2]))

else:
    max_score = [sum(stairs)]
print(max_score[-1])
