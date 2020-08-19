# 배열을 시계방향으로 90도 회전 하는 함수
def turn(x, rList):  # 배열의 길이 x, 기존의 배열 rList
    new_arr = [[0] * N for a in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = rList[N - j - 1][i]
    return new_arr


# up을 기준으로 하는 코드이므로, 밀고 싶은 방향을 up으로 맞춰주기
# up 0번, left 1번, down 2번, right 3번 회전시켜주면 된다.
# 회전시켜주는 함수
def switch(directions):
    change = {
        'up': 0,
        'left': 1,
        'down': 2,
        'right': 3,
    }
    directionNum = change.get(directions)
    return directionNum


# T = 1
T = int(input())
for t in range(1, T + 1):
    N, direction = input().split()  # N 배열크기, direction 방향
    N = int(N)
    arr = [list(map(int, input().split())) for i in range(N)]  # N X N 배열만들기

    # # 확인-----
    # print('입력값 확인')
    # print(N, direction)
    # for i in arr:
    #     print(i)
    # print()
    # # -----확인
    swdirec = switch(direction)
    for k in range(swdirec):
        arr = turn(N, arr)

    # # 확인 -----
    # print('회전확인')
    # for i in arr:
    #     print(i)
    # print()
    # # -----확인

    # up 기준
    # 0을 제외한 나머지 같은 숫자들 합치기
    for i in range(N):
        for j in range(N - 1):
            chk = 1
            while arr[j][i] != 0 and (j + chk) < N:  # 첫번째 위치가 0이면 생략 j+chk 가 N보다 크거나 같을경우 out of range 오류 이므로
                if arr[j][i] == arr[j + chk][i]:  # 첫번째와 두번째가 같으면
                    arr[j][i] *= 2  # 첫번째를 두배
                    arr[j + chk][i] = 0  # 두번째를 0
                    break  # 확인 종료
                elif arr[j + chk][i] != 0:  # 두번째가 0이 아니면
                    break  # 확인 종료
                chk += 1  # 두번째가 0이면 첫번째와 세번째를 비교하기 위해 chk 를 1 더해준다

    # # 확인-----
    # print('숫자합치기 확인')
    # for i in arr:
    #     print(i)
    # print()
    # # -----확인

    # 0을 제외한 나머지 숫자들을 up방향으로 밀기
    for i in range(N):
        for j in range(N - 1):
            if arr[j][i] == 0:  # 선택한 점이 0일때
                chk = 1
                while j + chk < N:
                    if arr[j + chk][i] != 0:  # 그 다음점이 0이 아니면
                        arr[j][i] = arr[j + chk][i]  # 다음점을 선택한 점에 덮어쓰기
                        arr[j + chk][i] = 0  # 그리고 다음점은 0
                        break  # 체크 종료
                    chk += 1  # 그 다음점도 0이라면 그 다다음점을 확인하기 위해 chk +1

    # # 확인-----
    # print('숫자밀기 확인')
    # for i in arr:
    #     print(i)
    # print()
    # # -----확인

    # 기존의 배열을 회전했으므로 다시 원래대로 돌리기 위해 4-swich(dirction) 번 회전시켜줌
    if swdirec != 0:  # up일경우 할 필요가 없다.
        for k in range(4 - swdirec):
            arr = turn(N, arr)

    # # 확인-----
    # print('최종 확인')
    # for i in arr:
    #     print(i)
    # print()
    # # -----확인

    # 답 출력하기
    print('#{}'.format(t))
    for i in range(N):
        result = ""
        for j in range(N):
            result += str(arr[i][j]) + ' '
        print(result)