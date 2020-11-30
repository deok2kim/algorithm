def is_k():
    if r - 1 < len(arr) and c - 1 < len(arr[0]):
        if arr[r - 1][c - 1] == k:
            return True

    return False


def update_arr():
    # 개수 세기
    tmp_matrix = []
    max_length = 0
    for i in range(len(arr)):
        numbers = set(arr[i])
        tmp_lst = []
        for num in numbers:
            if num == 0:
                continue
            tmp_lst.append((num, arr[i].count(num)))
        max_length = max(max_length, len(tmp_lst) * 2)
        tmp_matrix.append(tmp_lst)

    # 정렬하기
    for i in range(len(tmp_matrix)):
        tmp_matrix[i].sort(key=lambda x: (x[1], x[0]))

    # 길이 맞추기고 배열에 넣기
    for i in range(len(tmp_matrix)):
        tmp_lst = []
        for j in range(len(tmp_matrix[i])):
            tmp_lst.append(tmp_matrix[i][j][0])
            tmp_lst.append(tmp_matrix[i][j][1])
        tmp_lst.extend([0] * (max_length - len(tmp_lst)))
        arr[i] = tmp_lst


if __name__ == '__main__':
    r, c, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(3)]

    time = 0
    while time < 101:

        # k 값 맞는지 확인
        if is_k():
            print(time)
            break

        time += 1  # 시간 증가
        # R연산 vs C연산
        if len(arr) >= len(arr[0]):  # 행의 개수가 열의 개수보다 크거나 같으면
            update_arr()
        else:  # 행의 개수가 열의 개수보다 적으면
            arr = list(map(list, zip(*arr)))  # 행과 열 바꾸기
            update_arr()
            arr = list(map(list, zip(*arr)))  # 다시 행과 열 바꾸기
    else:
        print(-1)
