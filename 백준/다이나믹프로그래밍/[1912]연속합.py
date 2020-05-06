import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

# print(numbers)

result = -1001
max_sum = [0] * (n)

for i in range(n):
    max_sum[i] = max(numbers[i] + max_sum[i - 1], numbers[i])
    result = max(result, max_sum[i])
    # print(result, max_sum)

print(result)