def go_path(f):
    global answer

    check = [0] * N  # 다리를 건설했던 땅 체크 1이면 건설
    j = 0
    while j < N - 1:
        # 높이가 같을 때
        if f[j] == f[j + 1]:
            pass
        # 다음이 높을 때
        elif f[j] + 1 == f[j + 1]:
            # 다음 이전의 L 칸이 같은 높이 일때 and 다리 건설 안했을 때
            k = j
            cnt = 0
            while k >= 0:
                if k >= 0 and check[k] == 0 and f[k] == f[j]:
                    cnt += 1
                    check[k] = 1
                else:
                    return False
                if cnt == L:
                    break
                k -= 1
            # 건설할 수 있는 도로가 L보다 작으면
            if cnt < L:
                return False

        # 다음이 낮을 때
        elif f[j] - 1 == f[j + 1]:
            # 다음 같은 칸들이 L 과 같을 때
            k = j + 1
            cnt = 0
            while k < N:
                if k >= 0 and check[k] == 0 and f[k] == f[j + 1]:
                    cnt += 1
                    check[k] = 1
                else:
                    return False
                if cnt == L:
                    break
                k += 1
            # 건설할 수 있는 도로가 L보다 작으면
            if cnt < L:
                return False

        # 다음이 두칸 이상 차이 날 때
        else:
            return False
        j += 1
    return True


if __name__ == '__main__':
    N, L = map(int, input().split())  # N 배열 크기, L 경사로 길이
    field = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # 가로
    for i in field:
        if go_path(i):
            answer += 1
    # 세로
    for i in zip(*field):
        if go_path(i):
            answer += 1

    print(answer)
