def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]


def union(x, y):
    # a와 b의 대표자를 찾음
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    elif rank[py] > rank[px]:
        p[px] = py
    else:
        p[px] = py
        rank[py] += 1


# 1부터 8까지 해보자
n = 8
p = [0] * (n + 1)
rank = [0] * (n + 1)
for i in range(1, n + 1):
    make_set(i)

union(1, 3)
union(2, 3)
union(5, 6)
union(6, 8)
union(1, 5)
union(6, 7)
print(p)
print(find_set(4))
print(find_set(5))

# 연산의 효율을 높이는 방법
# 1. path compression: 모든 노드들이 직접 root를 가리키도록 갱신한다.
# 2. Rank를 이용한 Union: 각 노드는 자신을 루트로 하는 subtree의 높이를 Rank라는 이름으로 저장한다.
# 2-2. 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다.
