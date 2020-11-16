# 실패.....
import sys


def dfs(a: int, b: int, c: int, total: str):
    # 끝내기
    if a > work_day[0] or b > work_day[1] or c > work_day[2]:
        return

    if a == work_day[0] and b == work_day[1] and c == work_day[2]:
        print(total)
        sys.exit()

    for people in P:
        # A는 매일 일함
        if people == 'A':
            dfs(a + 1, b, c, total + people)
        # B는 전날 안하면 일함
        elif people == 'B' and total[-1] != 'B':
            dfs(a, b + 1, c, total + people)
        # C는 전날, 전전날 안하면 일함
        elif people == 'C':
            if len(total) == 1 and total[-1] != 'C':
                dfs(a, b, c + 1, total + people)
            elif len(total) >= 2 and total[-1] != 'C' and total[-2] != 'C':
                dfs(a, b, c + 1, total + people)


if __name__ == '__main__':
    S = input()
    # 각 사람의 일한 날짜 세기
    P = ('A', 'B', 'C')
    work_day = [S.count(people) for people in P]
    dfs(1, 0, 0, 'A')
    dfs(0, 1, 0, 'B')
    dfs(0, 0, 1, 'C')
