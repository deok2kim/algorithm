from itertools import permutations

N, M = map(int, input().split())

# 1부터 N 까지 M 개
for permu in permutations(range(1, N + 1), M):
    if M == 1:
        print(' '.join(list(map(str, permu))))
    else:
        for i in range(M - 1):
            if permu[i] > permu[i + 1]:
                break
        else:
            print(' '.join(list(map(str, permu))))
