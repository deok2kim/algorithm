T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = input().split()
    print('#{} {}'.format(t, numbers[m % n]))
