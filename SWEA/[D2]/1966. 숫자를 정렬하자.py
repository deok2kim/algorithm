T = int(input())
for t in range(1, T + 1):
    input()
    numbers = list(map(int, input().split()))
    numbers.sort()
    print('#{} {}'.format(t, ' '.join(list(map(str, numbers)))))
