from itertools import combinations

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

for i in range(1, N + 1):

    for combi in combinations(numbers, i):
        # print(combi)
        if sum(combi) == S:
            answer += 1

print(answer)
