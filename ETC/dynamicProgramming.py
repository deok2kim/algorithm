# 피보: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# 피보를 분할정복으로 구하는 방법
import time


def fibo1(x):
    if x == 1:
        return 1
    if x == 2:
        return 1

    return fibo1(x - 2) + fibo1(x - 1)


start = time.time()
print(fibo1(37))
end = time.time()
print(f'분할정복: {end - start}')

# 피보를 DP로 구하는 방법
dp = [0] * 100


def fibo2(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = fibo2(x - 2) + fibo2(x - 1)
    return dp[x]


start = time.time()
print(fibo2(37))
end = time.time()
print(f'다이나믹프로그래밍: {end - start}')

'''
24157817
분할정복: 6.408001184463501
24157817
다이나믹프로그래밍: 0.0
'''
