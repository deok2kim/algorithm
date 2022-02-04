from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for perm in (permutations(dungeons, len(dungeons))):
        cur_k = k
        expol_cnt = 0
        for dungeon in perm:
            if cur_k >= dungeon[0]:
                expol_cnt += 1
                cur_k -= dungeon[1]

        answer = max(answer, expol_cnt)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
