def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]


def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = p[px]
    elif rank[py] > rank[px]:
        p[px] = p[py]
    else:
        p[px] = p[py]
        rank[py] += 1


V, E = 7, 11
edges = [
    [0, 5, 60],
    [0, 1, 32],
    [0, 2, 31],
    [0, 6, 51],
    [1, 2, 21],
    [2, 4, 46],
    [2, 6, 25],
    [3, 4, 34],
    [3, 5, 18],
    [4, 5, 40],
    [4, 6, 51],
]

# 간선 정보를 가중치에 따라 오름차순으로 정렬
edges.sort(key=lambda x: x[2])

# 각 정점의 부모 정보, Rank 정보(효율성)
p = [0] * V
rank = [0] * V

# 각 정점의 부모를 자신으로 설정하기
for i in range(V):
    make_set(i)

# 간선을 선택하는 개수는 V-1개, 간선의 가중치를 누적한 결과값
cnt = 0
result = 0
for i in range(E):
    s, e, c = edges[i]

    # s와 e가 같은 집합이면( 사이클이면 ) 패쓰
    if find_set(s) == find_set(e):
        continue

    # 가중치를 더하고
    result += c

    # s와 e를 같은 집합으로 만든다
    union(s, e)

    # 간선을 V-1개 선택했으면 끝
    cnt += 1
    if cnt == V - 1:
        break

print(result)
