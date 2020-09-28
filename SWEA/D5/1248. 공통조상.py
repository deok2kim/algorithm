def find_parent(n, parent_list):
    if tree[n][2]:
        parent_list.append(tree[n][2])
        find_parent(tree[n][2], parent_list)


def find_common_parent(parent1, parent2):
    for p1 in parent1:
        for p2 in parent2:
            if p1 == p2:
                return p1


def find_subtree(n):
    global subtree_size
    for k in range(2):
        if tree[n][k]:
            subtree_size += 1
            find_subtree(tree[n][k])


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, 1 + T):
        # 정점수 V, 간선수 E, 공통조상을 찾는 두개의 정점번호 N1,N2
        V, E, N1, N2 = map(int, input().split())

        adj_list = list(map(int, input().split()))

        # 자식 노드, 자식 노드, 부모 노드
        tree = [[0] * 3 for _ in range(V + 1)]
        for i in range(E):
            s, e = adj_list[i * 2], adj_list[i * 2 + 1]
            if tree[s][0]:
                tree[s][1] = e
            else:
                tree[s][0] = e

            tree[e][2] = s

        # 각각의 부모 노드
        N1_parent, N2_parent = [], []
        find_parent(N1, N1_parent)
        find_parent(N2, N2_parent)

        # 공통 부모 노드
        common_parent = find_common_parent(N1_parent, N2_parent)

        # 공통 부모 노드 사이즈
        subtree_size = 1
        find_subtree(common_parent)

        print(f'#{tc} {common_parent} {subtree_size}')