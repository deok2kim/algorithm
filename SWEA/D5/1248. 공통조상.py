# 각각의 부모 노드 찾기
def find_parents(N, parents_list):
    if tree[N][2]:
        next_N = tree[N][2]
        parents_list.append(next_N)
        return find_parents(next_N, parents_list)

# 찾은 부모노드의 서브트리 갯수 세기
def find_subtree(N):
    global cnt
    if N != 0:
        cnt +=1
        find_subtree(tree[N][0])
        find_subtree(tree[N][1])


for tc in range(1, int(input())+1):
    V, E, N1, N2 = map(int, input().split())  # 정점의 수, 간선의 수, 공통 조상을 찾는 두개의 정점 번호
    tree = [[0]*3 for _ in range(V+1)]
    tmp = list(map(int, input().split()))

    # 트리 채우기
    for i in range(E):
        s, e = tmp[i*2], tmp[i*2+1]
        for j in range(3):
            if tree[s][j] == 0:
                tree[s][j] = e
                break
        tree[e][2] = s

    # 각각의 부모노드를 넣을 배열
    N1_parents, N2_parents = [], []
    find_parents(N1, N1_parents)
    find_parents(N2, N2_parents)

    # 공통 부모노드 찾기
    common_parent = 0
    for i in N1_parents:
        if i in N2_parents:
            common_parent = i
            break

    # 공통 부모노드의 서브트리 갯수 세기
    cnt = 0
    find_subtree(common_parent)

    print('#{} {} {}'.format(tc, common_parent, cnt))



'''
1
13 12 8 13
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 10 6 11 11 13
'''
