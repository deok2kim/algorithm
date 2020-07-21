def check():

    # 가로 검증
    for row in sudoku:
        if len(set(row)) != 9:
            return 0

    # 세로 검증
    numbers = set()
    for j in range(9):
        for i in range(9):
            numbers.add(sudoku[i][j])

        if len(numbers) != 9:
            return 0

        numbers.clear()

    # 네모 검증
    for l in range(3):
        for k in range(3):
            for i in range(k*3, k*3 + 3):
                for j in range(l*3, l*3 + 3):
                    numbers.add(sudoku[i][j])

            else:
                if len(numbers) != 9:
                    return 0

                numbers.clear()

    return 1

for tc in range(1, 1+ int(input())):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    for row in sudoku:
        print(row)

    print('#{} {}'.format(tc, check()))


