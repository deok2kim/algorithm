def solution(board, moves):
    answer = 0
    baguni = []
    len_board = len(board)
    for i in board:
        print(i)
    for i in moves:
        print(baguni)
        for j in range(len_board):
            if board[j][i-1] != 0:
                baguni.append(board[j][i-1])
                board[j][i - 1] = 0
                break

        if len(baguni) >= 2:
            if baguni[-1] == baguni[-2]:
                baguni.pop(-1)
                baguni.pop(-1)
                answer += 2

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
