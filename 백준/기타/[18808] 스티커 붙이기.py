# 스티커 시작점 찾기
def start_find():
    for i in range(notebook_sero):
        for j in range(notebook_garo):
            if stick(i, j):
                return True

    return False


def stick(i, j):
    # 겹치는지 판단하기
    for k in range(sticker_sero):
        for l in range(sticker_garo):
            if 0 <= i+k < notebook_sero and 0 <= j+l < notebook_garo:  # 스티커가 노트북 크기를 넘어가지 않을 때
                if sticker[k][l] == 1 and notebook[i + k][j + l] == 1:
                    return False
            else:
                return False

    # 스티커 붙이기
    for k in range(sticker_sero):
        for l in range(sticker_garo):
            if sticker[k][l] == 1:
                notebook[i + k][j + l] = 1

    return True


# 스티커 회전
def sticker_rotation():
    global sticker, sticker_sero, sticker_garo

    tmp_sticker = [[0]*sticker_sero for _ in range(sticker_garo)]
    for i in range(sticker_sero):
        for j in range(sticker_garo):
            tmp_sticker[j][sticker_sero-i-1] = sticker[i][j]

    sticker, sticker_sero, sticker_garo = tmp_sticker, len(tmp_sticker), len(tmp_sticker[0])
    return


notebook_sero, notebook_garo, sticker_count = map(int, input().split())
notebook = [[0]*notebook_garo for _ in range(notebook_sero)]

for _ in range(sticker_count):
    sticker_sero, sticker_garo = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(sticker_sero)]

    for _ in range(4):
        if start_find():
            break
        else:
            sticker_rotation()

# 노트북에 붙은 스커 갯수
result = 0
for i in range(notebook_sero):
    for j in range(notebook_garo):
        if notebook[i][j]:
            result += 1

print(result)
