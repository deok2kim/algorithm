T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))

    numbers.sort()
    print(numbers)
    print(numbers[1:-1])
    print('#{} {}'.format(t, round(sum(numbers[1:-1]) / 8)))
