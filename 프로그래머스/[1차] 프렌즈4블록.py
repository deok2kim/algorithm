def solution(m, n, board):

    def game():
        nonlocal answer, check

        check = 0
        for i in range(sero - 1):
            for j in range(garo - 1):
                if field[i][j] != ' ':
                    champ = field[i][j]
                    if field[i + 1][j] == champ and field[i][j + 1] == champ and field[i + 1][j + 1] == champ:
                        delete_list[i][j] = 1
                        delete_list[i + 1][j] = 1
                        delete_list[i][j + 1] = 1
                        delete_list[i + 1][j + 1] = 1

        # for i in delete_list:
        #     print(i)
        # print()

        for i in range(sero):
            for j in range(garo):
                if delete_list[i][j] == 1:
                    field[i][j] = ' '
                    delete_list[i][j] = 0
                    check += 1

        # for i in field:
        #     print(i)
        # print()

        # for i in delete_list:
        #     print(i)
        # print()

        checked_list = []
        for i in range(sero - 1, -1, -1):
            for j in range(garo):
                if j not in checked_list:
                    if field[i][j] == ' ':
                        y = i
                        cnt = 1
                        while y >= 0:
                            y -= 1
                            if field[y][j] == ' ':
                                cnt += 1
                            else:
                                break
                        else:
                            checked_list.append(j)
                        # print('바꾸기 : ', j, i, cnt, y)

                        for k in range(cnt):
                            if i - cnt - k >= 0:
                                field[i - k][j], field[i - cnt - k][j] = field[i - cnt - k][j], field[i - k][j]
                                # print('바꿈')
                                # for z in field:
                                #     print(z)
                                # print()
        # for i in field:
        #     print(i)
        # print()
        return check

    answer = 0
    field = [list(i) for i in board]
    # for i in field:
    #     print(i)
    # dy = [-1, 1, 0, 0]
    # dx = [0, 0, -1, 1]

    garo = len(field[0])
    sero = len(field)

    delete_list = [[0] * garo for _ in range(sero)]
    check = 1

    while check != 0:
        # print('시작')
        answer += game()
        # print(check)
    return answer


print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))
