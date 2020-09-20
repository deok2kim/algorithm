from itertools import combinations


def solution(N, stat):
    answer = float('inf')

    def cal_stat(team):
        # print('시작')
        team_stat = 0
        for i in range(len(team)):
            for j in range(i, len(team)):
                team_stat += stat[team[i]][team[j]]
                team_stat += stat[team[j]][team[i]]

        return team_stat

    all_members = set()
    for i in range(N):
        all_members.add(i)

    # for row in stat:
    #     print(row)
    # print()

    for i in range(1, N // 2 + 1):
        for com in combinations(all_members, i):
            start_team = list(com)
            link_team = list(all_members - set(start_team))
            a = cal_stat(start_team)
            b = cal_stat(link_team)
            answer = min(answer, abs(a - b))

    print(answer)
    return


if __name__ == "__main__":
    N0 = int(input())
    arr = [list(map(int, input().split())) for _ in range(N0)]
    solution(N0, arr)
