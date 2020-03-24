numbers = [1, 1, 1, 2, 2]

for tc in range(1, int(input()) + 1):
    n = int(input())
    for i in range(len(numbers) - 1, n + 1):
        numbers.append(numbers[i] + numbers[i - 4])

    # print(numbers)
    print(numbers[n - 1])
