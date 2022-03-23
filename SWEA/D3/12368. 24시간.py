T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().strip().split(' '))
    print(f'#{test_case}', a + b - 24 if a + b >= 24 else a + b)
