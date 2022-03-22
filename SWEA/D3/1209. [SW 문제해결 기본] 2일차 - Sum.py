T = 10  # 테케는 10개

for test_case in range(1, T + 1):
    input()  # 테케 번호 받기
    N = 100
    answer = 0
    arr = [list(map(int, input()[:-1].split(' '))) for _ in range(N)]  # 2 차원 행렬화
    # [:-1]을 한 이유는 맨 마지막에 띄어쓰기가 들어간다. 오랜만에 해서 왜 그런지 모르겠음

    # 가로 합
    for i in range(N):
        answer = max(sum(arr[i]), answer)

    vertical_sum_list = [0] * len(arr[0])
    # 세로 합
    for i in range(N):
        for j in range(N):
            vertical_sum_list[j] += arr[i][j]

    answer = max(max(vertical_sum_list), answer)

    # 대각선
    right_cross_sum = 0
    for i in range(N):
        right_cross_sum += arr[i][i]
    answer = max(answer, right_cross_sum)

    left_cross_sum = 0
    for i in range(N):
        left_cross_sum += arr[i][N - 1 - i]
    answer = max(answer, left_cross_sum)

    print(f'#{test_case} {answer}')
