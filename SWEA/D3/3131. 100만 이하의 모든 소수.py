N = 10 ** 6 + 1
eratos = [1] * N
eratos[0], eratos[1] = 0, 0

for i in range(2, N):
    if eratos[i] == 1:
        for j in range(i * 2, N, i):
            eratos[j] = 0

for i in range(N):
    if eratos[i] == 1:
        print(i, end=' ')
