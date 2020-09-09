def solution(m, n, board):
    answer = 0

    board = [list(board[i]) for i in range(m)]
    # print('=====최초=====')
    # for row in board:
    #     print(row)
    # print()

    while True:
        # 지울 거 찾기
        remove_list = set()

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != '0':
                    if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                        remove_list.add((i, j))
                        remove_list.add((i + 1, j))
                        remove_list.add((i, j + 1))
                        remove_list.add((i + 1, j + 1))

        # 지우기
        if not remove_list:
            break

        for r in remove_list:
            board[r[0]][r[1]] = '0'
            answer += 1

        # print('=====지우기=====')
        # for row in board:
        #     print(row)
        # print()

        # 정렬하기
        for j in range(n):
            x, y = m, 0  # 빈 곳

            for i in range(m - 1, -1, -1):

                if x == -1:
                    break
                if board[i][j] == '0' and x == m:
                    x, y = i, j
                elif board[i][j] != '0' and x < m:
                    board[x][y] = board[i][j]
                    board[i][j] = '0'
                    x -= 1

        # print('=====정렬하기=====')
        # for row in board:
        #     print(row)
        # print()

    return answer


print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print()
print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))
print()
print(solution(6, 6, ['TTTANT', 'RTFACC', 'TRRFCC', 'TRRRAA', 'TTTTTF', 'TTTTTJ']))
print()
