T = int(input())

for t in range(1, T + 1):
    a, b, c = map(int, input().split())
    cheap = min(a, b)
    result = c // cheap
    print('#{} {}'.format(t, result))

