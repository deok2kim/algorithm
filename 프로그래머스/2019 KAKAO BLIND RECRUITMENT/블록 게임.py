blocks = {
    1: [[
        (1, 0),
        (1, 1),
        (1, 2)
    ],
        [(0, 1), (0, 2)]]
    ,

    2: [[
        (1, 0),
        (1, -1),
        (1, -2)
    ],
        [(0, -1), (0, -2)]],
    3: [[
        (1, 0),
        (2, 0),
        (2, 1)
    ],
        [(1, 1)]],
    4: [[
        (1, 0),
        (2, 0),
        (2, -1)
    ],
        [(1, -1)]],
    5: [[
        (1, 0),
        (1, -1),
        (1, 1)
    ],
        [(0, -1), (0, 1)]],
}


def solution(board):
    answer = 0
    n = len(board)

    # 지울 수 있는 블록인지 아닌지 체크
    def block_check(x, y, idx):
        for block, d in blocks.items():
            for k in range(3):
                nx = x + d[0][k][0]
                ny = y + d[0][k][1]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] != idx:
                        break
                else:
                    break
            else:
                return block
        else:
            return 0

    # 지우러 들어가기 먼저 체크부터하고
    def remove_check(x, y, shape, idx):
        nonlocal answer
        for dx, dy in blocks[shape][1]:
            cx = x + dx
            cy = y + dy
            while cx >= 0:
                if board[cx][cy] == 0:
                    cx -= 1
                else:
                    # 못 지움 - 위가 다른 블록으로 막혀있음
                    if idx not in temp_list:
                        temp_list.add(idx)
                        temp_dict[idx] = [x, y, shape]
                    return False

        else:
            # 지울 수 있는 조건을 만족해서 지우기
            board[x][y] = 0
            for k in range(3):
                board[x + blocks[shape][0][k][0]][y + blocks[shape][0][k][1]] = 0
            answer += 1
            return True

    never_list = set()  # 블록이 아예 못지우는 형태
    temp_list = set()  # 지울 수 있는 블럭이지만 가로막혀서 못지우고 있는 애
    temp_dict = {}  # 그 애의 초기 위치

    # 시작!! - 블록 찾기
    for i in range(n):
        for j in range(n):
            K = board[i][j]
            if K and K not in never_list and K not in temp_list:
                shape = block_check(i, j, K)
                if shape:  # 내가 원하는 블록(지울 수 있는 블록) 이면
                    if remove_check(i, j, shape, K):  # 지울 수 있는지 체크하러 ㄱㄱ
                        if temp_list:  # 못 지웠떤 애들 다시 지워볼까?
                            for key, value in temp_dict.items():
                                if key in temp_list:
                                    remove_check(value[0], value[1], value[2], key)
                                    temp_list.remove(key)
                else:
                    never_list.add(K)

    return answer


# print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
#                 [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
#                 [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))

# print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [4, 0, 7, 0, 0, 0, 0, 0, 0, 0],
#                 [4, 7, 7, 7, 0, 0, 0, 0, 0, 0],
#                 [4, 4, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
#                 [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
#                 [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
