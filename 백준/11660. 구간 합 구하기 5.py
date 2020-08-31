import sys
from itertools import accumulate  # 누적 합을 구해주는 내장함수

if __name__ == "__main__":
    N, M = map(int, input().split())
    numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 0,0 부터 n1,n2까지 각각의 합을 미리 구해놓기
    for i in range(N):
        numbers[i] = list(accumulate(numbers[i]))
    for i in range(1, N):
        for j in range(N):
            numbers[i][j] += numbers[i-1][j]
    print()
    for row in numbers:
        print(row)

    orders = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    for x1, y1, x2, y2 in orders:
        all = numbers[x2-1][y2-1]  # 전체

        if x1 == 1 and y1 == 1:
            print(all)
            continue

        minus2 = numbers[x2 - 1][y1 - 2]  # 뺄부분 1
        minus1 = numbers[x1 - 2][y2 - 1]  # 뺄부분 2
        if x1 == 1:
            print(all-minus2)
        elif y1 == 1:
            print(all-minus1)
        else:
            plus = numbers[x1 - 2][y1 - 2]  # 중복으로 빼서 다시 더해야될 부분
            print(all-minus1-minus2+plus)
