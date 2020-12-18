# 인풋
T = int(input())
Ns = [int(input()) for _ in range(T)]

# 풀이
# N-3 + N-2 = N, 피보나치랑 비슷, 숫자가 나올때 마다 구하면 시간이 오래걸리므로 한번에 구해놓고 해결하자.
pado = [1, 1, 1]
for i in range(3, 101):  # N 의 범위가 100 까지
    pado.append(pado[i - 3] + pado[i - 2])

# 결과 출력
for tc in range(T):
    print(f'#{tc + 1} {pado[Ns[tc] - 1]}')
