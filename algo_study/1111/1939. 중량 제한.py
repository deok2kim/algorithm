import math

n, m = map(int, input().split())
mp = [[] for _ in range(n + 1)]
mx = 0
for _ in range(m):
    st = list(map(int, input().split()))
    mp[st[0]].append((st[1], st[2]))
    mp[st[1]].append((st[0], st[2]))
    if mx < st[2]:
        mx = st[2]
st, ed = map(int, input().split())
val = math.log2(n)
val = int(val)
d = [[False for _ in range(n + 1)] for __ in range(val + 30)]
start, end, cnt = 0, mx, 0
while start <= end:
    q = list()
    mid = (start + end) // 2
    q.append(st)
    d[cnt][st] = True
    goal = False
    while q:
        x = q.pop(0)
        if x == ed:
            goal = True
            break
        for v in mp[x]:
            next_node = v[0]
            value = v[1]
            if d[cnt][next_node]:
                continue
            if value < mid:
                continue
            d[cnt][next_node] = True
            q.append(next_node)
    if goal:
        start = mid + 1
    else:
        end = mid - 1
    cnt += 1
print(end)
