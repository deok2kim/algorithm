gear = [list(input()) for _ in range(4)]  # 톱니
k = int(input())  # 회전수

for i in range(k):
    n, d = map(int, input().split())
    n -= 1  # 톱니바퀴 인덱스는 0부터

    # 0번 12시방향, 2번 오른쪽, 6번 왼쪽
    pole = []  # 각 톱니의 왼쪽과 오른쪽을 배열에 저장
    rotationCheck = [0]*4  # 회전을 할지 말지 저장
    ds = [1, -1, 1, -1]  # 각 톱니의 회전 방향

    while True:  # 처음 회전할 톱니의 방향을 결정하고 그 방향에 따라 나머지를 반대방향으로 설정해준다.
        if ds[n] == d:
            break
        else:
            ds = ds[3:] + ds[:3]

    for j in range(4):  # 각 톱니의 왼쪽과 오른쪽을 배열에 저장
        pole.append(gear[j][6])
        pole.append(gear[j][2])

    br = n * 2 - 1  # 현재 기준 왼쪽 톱니의 오른쪽
    cl = n * 2      # 현재 기준 현재 톱니의 왼쪽

    cr = n * 2 + 1  # 현재 기준 현재 톱니의 오른쪽
    nl = n * 2 + 2  # 현재 기준 오른쪽 톱니의 왼쪽

    # 왼쪽 톱니 확인
    while True:
        if br < 1:
            break

        if pole[br] != pole[cl]:
            rotationCheck[br // 2] = 1
            rotationCheck[br // 2 + 1] = 1
            br -= 2
            cl -= 2
        else:
            break

    # 오른쪽 톱니 확인
    while True:
        if nl > 6:
            break

        if pole[cr] != pole[nl]:
            rotationCheck[cr // 2] = 1
            rotationCheck[cr // 2 + 1] = 1
            cr += 2
            nl += 2
        else:
            break

    if sum(rotationCheck) == 0:  # 맞물리는 톱니가 없을 때 혼자 회전
        if d == -1:
            gear[n] = gear[n][1:] + gear[n][:1]
        elif d == 1:
            gear[n] = gear[n][7:] + gear[n][:7]

    else:
        for j in range(4):
            if rotationCheck[j] == 1:
                if ds[j] == -1:  # 반시계
                    gear[j] = gear[j][1:] + gear[j][:1]

                elif ds[j] == 1:  # 시계
                    gear[j] = gear[j][7:] + gear[j][:7]

# 톱니의 점수 계산
result = 0
for i in range(4):
    if gear[i][0] == '1':
        result += 2**i

print(result)
