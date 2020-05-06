import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

# print(numbers)

result = -1001
min_sum = [0] * (n)

for i in range(n):
    min_sum[i] = max(numbers[i] + min_sum[i - 1], numbers[i])
    result = max(result, min_sum[i])
    # print(result, max_sum)

print(result)