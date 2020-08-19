T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))

    result = set()
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1,7):
                result.add(numbers[i]+numbers[j]+numbers[k])

    result = list(result)
    result.sort(reverse=True)
    print('#{} {}'.format(t, result[4]))
