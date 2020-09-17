from itertools import permutations


# 외벽을 점검할 순서를 결정하는 것
def lotation_wall(wall):
    print(wall)
    for i in range(len(wall)):
        if wall[i] == 1:
            return wall[i+1:]+wall[:i+1]


# 외벽 수리
def repair(dist_permu, wall):
    idx = 0  # 벽의 인덱스
    for i in range(len(dist_permu)):

        dist = dist_permu[i]  # 점검할 친구를 하나 꺼내서
        while idx < len(wall):
            if wall[idx] == 1:  # 취약점을 만나면
                idx += dist + 1  # 다음 취약점으로 건너 뛴다.

                # 마지막 외벽 점검
                if idx >= len(wall):  # 건너 뛰었는데 벽이 더 이상 없으면 다 점검했으므로 끝
                    return i + 1

                break  # 이번 친구는 점검을 마쳤으므로 다음 친구가 오기 위해서 점검 while 문을 끝낸다.

            idx += 1
        else:
            # 마지막인줄 모르고 친구한명 더 투입 시켰을 때
            # 친구가 점검하러 나갔는데 더 이상 취약점이 없을 때
            return i

    else:
        # 친구 다 투입했는데 점검 끝내지 못함
        # 취약점이 아직 남았을 때
        return 10


def solution(n, weak, dist):
    # 취약점 나열하기
    wall = [0]*n
    for w in weak:
        wall[w] = 1

    # 결과 값들 저장
    result = []

    # 고칠 순서 정하기
    length_dist = len(dist)
    for d in permutations(dist, length_dist):
        # 처음 취약 점 순서로 탐색
        # print(d)
        re_wall = wall
        result.append(repair(d, re_wall))

        # 취약 점 순서를 바꿔가며 탐색
        for i in range(length_dist):
            re_wall = lotation_wall(re_wall)
            result.append(repair(d, re_wall))

    # 결과 중에서 가장 작은 값 선택
    answer = min(result)
    # 만약 작은 값이 10(외벽점검실패)라면 -1 반환
    if answer == 10:
        answer = -1
    return answer

print(solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4]))