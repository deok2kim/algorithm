# 사다리 타기
def down():
    # 1,1 부터 시작!
    for start in range(1, N+1):
        y = start  # 시작점 인덱스를 저장
        for i in range(1, H+1):
            # 내려갔는데 1을 만나면 오른쪽으로
            if ladder[i][y] == 1:
                y += 1
            # 그게아니라 왼쪽을 봤는데 1을 봤으면 왼쪽으로
            elif ladder[i][y-1] == 1:
                y -= 1

        else:
            # 도착점이 시작점과 같지 않으면 False
            if start != y:
                return False
    # 같으면 True
    else:
        return True


# 사다리 짓기
def build(idx, tmp_cnt):
    global result
    if result > -1:
        return

    # 사다리를 원하는 갯수만큼 지었을 때
    if tmp_cnt == cnt:
        # 사다리 타기를 해서 True면 끝!
        if down():
            result = cnt
        return

    for i in range(idx, H+1):  # idx~H+1 : 다시 맨위부터 사다리를 만드는 것을 방지!
        for j in range(1, N):  # 1~N : 사다리는 항상 왼쪽에 만들기 때문에 N+1이 아닌 N까지!
            # 결과를 얻었을 때 모든 함수를 바로바로 리턴하려고
            # 혹시나 시간 짧아질까 넣어둠
            if result > -1:
                return
            # 현재위치, 왼쪽, 오른쪽에 사다리가 없으면 사다리를 만들자
            if ladder[i][j] == 0 and ladder[i][j-1] == 0 and ladder[i][j+1] == 0:
                ladder[i][j] = 1  # 사다리 만들고
                build(i, tmp_cnt+1)  # 다음으로 넘어간다음 나와서
                ladder[i][j] = 0  # 사다리 없애고

    return


N, M, H = map(int, input().split())  # 전체 세로줄, 가로 그어져 있는 줄, 전체 가로줄
ladder = [[0]*(N+2) for _ in range(H+1)]  # 1,1부터 시작하므로, 양옆에 0으로 채우고, 맨위에도 0으로 채운다.

# (건너는)가로줄 다리의 왼쪽을 1로 둔다 | 사다리를 내려올 때, 내려온 지점과 그 지점의 왼쪽을 항상 탐색 할 것
for _ in range(M):
    x, y = map(int, input().split())
    ladder[x][y] = 1

# 사다리를 3개까지 둬도 정답이 없으면 -1
result = -1
for cnt in range(4):
    build(1, 0)
    # 정답을 찾으면 break!
    if result != -1:
        break

print(result)



'''
5 5 6
1 1
3 2
2 3
5 1
5 4
'''