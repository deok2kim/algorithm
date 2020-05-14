def level_check(street):
    idx = 0
    cur_level = street[idx]  # 현재 높이
    build = [0]*n  # 경사로를 이미 지었는지 여부
    while idx < n-1:
        befo_level = cur_level
        idx += 1
        cur_level = street[idx]
        # 현재 위치의 높이와 전의 위치의 높이를 비교
        # 높이가 같을 때
        if cur_level == befo_level:
            continue

        # 높이가 전보다 두칸 이상 작을 때
        elif cur_level < befo_level - 1:
            return 0

        # 전보다 한칸 작을 때!!!
        elif cur_level == befo_level - 1:
            if n - idx < l:  # 남은 인덱스가 부족한 경우  (경사로를 l 길이 만큼 지을 공간이 부족할 때)
                return 0

            for j in range(l):
                # 지어야할 경사로의 높이가 같은지 확인 & 이미 경사로를 지었는지 확인
                if street[idx+j] == cur_level and build[idx+j] == 0:
                    build[idx+j] = 1
                    continue
                else:
                    return 0
            else:
                idx = idx+j  # 경사로를 앞으로 지었으므로 그만큼 인덱스를 건너뜀
                cur_level = street[idx]

        # 전보다 두칸 이상 클 때
        elif cur_level > befo_level + 1:
            return 0

        # 전보다 한칸 클 때!!! (경사로를 앞으로 지어야 한다)
        elif cur_level == befo_level +1:
            if idx < l:  # 남은 인덱스가 부족한 경우  (경사로를 l 길이 만큼 지을 공간이 부족할 때)
                return 0

            for j in range(l):
                # 지어야할 경사로의 높이가 같은지 확인 & 이미 경사로를 지었는지 확인
                if street[idx-j-1] == befo_level and build[idx-j-1] == 0:
                    build[idx - j - 1] = 1
                    continue
                else:
                    return 0
            # 경사로를 뒤로 지었으므로 인덱스를 건너 뛸 필요가 없다.

    return 1


###################################################################################################
n, l = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    cnt += level_check(field[i])  # 가로
    cnt += level_check([k[i] for k in field])  # 세로

print(cnt)
