from _collections import deque

# 디큐를 쓰는 이유는 시간효율
# 문제에 주어진 4가지를 계산하는 함수
def cal(number, idx):
    if idx == 0:
        return number+1
    elif idx == 1:
        return number-1
    elif idx == 2:
        return number*2
    else:
        return number-10


# BFS 탐색
# BFS를 쓰는 이유는 단계별로 탐색을 해야 하기 때문
def bfs():
    q = deque()
    q.append((n, 0))
    while q:
        number, cnt = q.popleft()  # 계산한 수와 그 숫자를 몇번째에서 얻었는지를 뽑는다.

        if number == m:  # 뽑은 숫자가 내가 원하는 숫자이면 cnt를 리턴
            return cnt

        for i in range(4):  # 그게 아니라면 그 숫자에 대해서 4가지 계산을 해준다.
            next_number = cal(number, i)

            if 0 < next_number <= 1000000 and dp[next_number] == 0:  # 백만 이하의 자연수 이면서, 아직 얻은 적이 없는(방문하지 않은) 숫자라면
                dp[next_number] = 1  # 그 숫자에 대해서 방문 표시를 해주고
                q.append((next_number, cnt+1))  # 그 숫자에 대해서 다음 단계를 하기 위해 cnt+1을 넣어준다.


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    dp = [0] * 1000001  # 백만 이하의 자연수 | 여기서는 visit 배열과 유사하다.
    dp[n] = 1
    result = bfs()
    print('#{} {}'.format(tc, result))
