from itertools import combinations


# 팀 나누기 - set 이용
def split_team(a_team, idx):
    global answer
    if len(a_team) == len(all_team) // 2:
        b_team = all_team - a_team
        answer = min(answer, abs(sum_stat(a_team) - sum_stat(b_team)))
        return

    for i in range(idx, len(all_team)):
        a_team.add(i)
        split_team(a_team, i + 1)
        a_team.remove(i)


# 팀 스탯 계산하기
def sum_stat(team):
    stat = 0
    for player1, player2 in combinations(team, 2):
        stat += table[player1][player2] + table[player2][player1]

    return stat


if __name__ == '__main__':
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    all_team = set(i for i in range(N))
    answer = float('inf')

    split_team(set(), 0)

    print(answer)
