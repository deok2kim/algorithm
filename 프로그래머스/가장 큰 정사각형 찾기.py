# DP을 알게 해준 코드
# Dynamic Programming이란 점화식과 비슷한 듯하다.
# 전에 나왔던 답을 이용해서 효율적으로 다음 답을 캐치하는 것이다.
# F(n) = F(n-1) + F(n-2) 꼴을가진 피보나치 수열도 Dynamic Programming의 일부라고 볼 수 있다.


def solution(board):
    sero = len(board)
    garo = len(board[0])

    # 모든 값이 0인 경우
    max_rec = max([num for row in board for num in row])
    if max_rec == 0:
        return 0

    for i in range(1, sero):
        for j in range(1, garo):
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

    max_rec = max([num for row in board for num in row])

    return max_rec ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4
print(solution([[0, 0, 1, 0]]))
print(solution([[0, 0, 0, 0], [0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]))  # 9
