def start_find(tetro):
    for i in range(paper_sero - len(tetro) + 1):
        for j in range(paper_garo - len(tetro[0]) + 1):
            stick(i, j, tetro)


def stick(i, j, tetro):
    sum_num = 0
    for k in range(len(tetro)):
        for l in range(len(tetro[0])):
            if tetro[k][l] == 1:
                sum_num += paper[i+k][j+l]

    result.append(sum_num)


def rotation(tetro):
    tetro_sero = len(tetro)
    tetro_garo = len(tetro[0])
    tmp_tetro = [[0] * tetro_sero for _ in range(tetro_garo)]
    for i in range(tetro_sero):
        for j in range(tetro_garo):
            tmp_tetro[j][tetro_sero - i - 1] = tetro[i][j]

    return tmp_tetro


paper_sero, paper_garo = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(paper_sero)]

tetrominos = {
    'ㅡ': [[1, 1, 1, 1]],
    'ㅁ': [[1, 1], [1, 1]],
    'ㅜ': [[1, 1, 1], [0, 1, 0]],
    'ㄱ': [[1, 1, 1], [0, 0, 1]],
    'ㄱㄱ': [[1, 1, 1], [1, 0, 0]],
    'ㄹ': [[0, 1, 1], [1, 1, 0]],
    'ㄹㄹ': [[1, 1, 0], [0, 1, 1]]
}

result = []
for key, tetromino in tetrominos.items():
    if key == 'ㅡ' or key == 'ㄹ' or key == 'ㄹㄹ':
        for i in range(2):
            start_find(tetromino)
            if  i == 1 :
                break

            tetromino = rotation(tetromino)

    elif key == 'ㅁ':
        start_find(tetromino)

    else:
        for i in range(4):
            start_find(tetromino)
            if i == 3:
                break

            tetromino = rotation(tetromino)

print(max(result))