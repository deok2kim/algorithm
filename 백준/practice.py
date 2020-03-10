import sys
input = sys.stdin.readline
print = sys.stdout.write
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
def main():
    test_case = int(input())
    for _ in range(test_case):
        num = int(input())
        for iter in range(4, num + 1):
            dp[iter] = dp[iter - 1] + dp[iter - 2] + dp[iter - 3]
        print(str(dp[num]))
        print("\n")
    return
main()