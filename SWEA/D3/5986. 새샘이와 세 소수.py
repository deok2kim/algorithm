prime = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

for tc in range(int(input())):
    N = int(input())
    M = len(prime)
    cnt = 0
    for i in range(M):
        if prime[i] > N:
            break
        for j in range(i, M):
            if prime[j] > N:
                break
            for k in range(j, M):
                if prime[k] > N:
                    break

                if prime[i] + prime[j] + prime[k] == N:
                    cnt += 1

    print(f'#{tc + 1} {cnt}')
