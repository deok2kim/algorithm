from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))

result = []
for permu in permutations(numbers, n):
    tmp = 0
    for i in range(n - 1):
        tmp += abs(permu[i] - permu[i + 1])
    result.append(tmp)

print(max(result))
