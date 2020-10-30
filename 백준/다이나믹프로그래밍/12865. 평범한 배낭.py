import sys

input = sys.stdin.readline
N, M = map(int, input().split())  # 물품 수, 최대 무게
items = [tuple(map(int, input().split())) for _ in range(N)]
# print(items)

dp = [[0] * (M + 1) for _ in range(N + 1)]
# for row in dp:
#     print(row)
# print()

for item_idx in range(1, N + 1):
    for weight in range(1, M + 1):
        item_weight, item_value = items[item_idx - 1]

        # 계산단계의 무게가 물건의 무게보다 작아서 아직 해당 단계의 물건을 못넣음
        if weight < item_weight:
            dp[item_idx][weight] = dp[item_idx - 1][weight]
        else:
            dp[item_idx][weight] = max(dp[item_idx - 1][weight], dp[item_idx - 1][weight - item_weight] + item_value)

        # for row in dp:
        #     print(row)
        # print()

print(dp[-1][-1])
