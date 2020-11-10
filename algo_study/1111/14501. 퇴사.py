import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    schedule = [tuple(map(int, input().split())) for _ in range(N)]
    profit = [0] * (N + 1)
    max_profit = 0
    for i in range(N - 1, -1, -1):
        day, money = schedule[i]
        if i + day > N:
            profit[i] = max_profit
            continue
        else:
            max_profit = max(money + profit[i + day], max_profit)
            profit[i] = max_profit
    print(max_profit)
