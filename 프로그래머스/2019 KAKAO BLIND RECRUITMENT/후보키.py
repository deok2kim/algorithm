from itertools import combinations as combi


def solution(relation):
    answer = 0
    N = len(relation)
    new_relation = {}
    candidates = set()
    column = []

    # for key, value in new_relation.items():
    #         print(f'{key}: {value}')

    # 옆으로 돌리면서 1개짜리 거르기
    for idx, i in enumerate(zip(*relation)):
        # print(i)
        if len(i) == len(set(i)):
            answer += 1
        else:
            new_relation[idx] = i
            column.append(idx)

    for n in range(2, len(relation[0]) + 1):
        for p in combi(column, n):
            # print()
            # print(n, p)
            # print(candidates)
            # 후보자격이 될 수 있는 지 체크
            for candidate in candidates:
                # print(candidate, p)
                cnt = 0
                for a in p:
                    if a in candidate:
                        cnt += 1

                else:
                    if cnt == len(candidate):
                        break

            else:

                # 후보자격이 될 수 있다면, 후보가 될 수 있는지 체크
                check_set = set()
                for i in range(N):
                    tmp = ''
                    for j in p:
                        tmp += new_relation[j][i]

                    check_set.add(tmp)

                else:
                    if len(check_set) == N:
                        candidates.add(p)

                # print(f'candidates: {candidates}')

    answer += len(candidates)
    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
