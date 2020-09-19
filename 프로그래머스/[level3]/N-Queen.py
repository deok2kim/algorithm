def solution(n):
    answer = 0
    chess = [[0] * n for _ in range(n)]  # 체스판
    visited = [0] * (n + 1)  # 세로칸 방문 체크

    # 조건에 일치 하는 지 체크 | 왼쪽 대각선, 오른쪽 대각선
    def check(x, y):
        ly, ry = y, y
        while x >= 0:
            x -= 1
            ly -= 1
            ry += 1
            if 0 <= ly:  # 왼쪽 대각선
                if chess[x][ly]:
                    return False

            if ry < n:  # 오른쪽 대각선
                if chess[x][ry]:
                    return False

        return True

    def bt(idx=0):
        nonlocal answer
        if idx == n:  # 체스를 마지막칸까지 두는데 성공한 경우
            answer += 1
            return

        for i in range(n):
            if visited[i] == 0:  # 세로 칸에 둔 말이 없는 경우
                if check(idx, i):  # 대각선방향 체크
                    chess[idx][i] = 1  # 체스판에 말을 두고
                    visited[i] = 1  # 이제 i 칸(세로 전체)는 말을 못둔다.
                    bt(idx + 1)
                    chess[idx][i] = 0
                    visited[i] = 0

    bt()

    return answer


print(solution(4))
