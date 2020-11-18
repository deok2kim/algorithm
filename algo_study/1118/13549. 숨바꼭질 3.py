from _collections import deque


def zero_one_bfs(n, k):
    q = deque()
    q.append(n)

    MX = 100001
    key = [0] * MX
    while q:
        x = q.popleft()

        if x == k:
            return key[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MX and not key[nx]:
                if nx == x * 2 and x:
                    key[nx] = key[x]
                    q.appendleft(nx)
                else:
                    key[nx] = key[x] + 1
                    q.append(nx)


if __name__ == '__main__':
    N, K = map(int, input().split())

    answer = zero_one_bfs(N, K)
    print(answer)