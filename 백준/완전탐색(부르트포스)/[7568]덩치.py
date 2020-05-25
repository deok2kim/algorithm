N = int(input())
hulk = [list(map(int, input().split())) for _ in range(N)]

# 자신보다 큰사람 숫자세기
cnt_list = [0] * N
for i in range(N):
    cnt = 1 # 등수는 1등부터 있으므로 1부터 시작
    for j in range(N):
        # 무게와 키가 자신보다 크다면 +1
        if hulk[i][0] < hulk[j][0] and hulk[i][1] < hulk[j][1]:
            cnt += 1
    else:
        cnt_list[i] = str(cnt)

print(' '.join(cnt_list))
