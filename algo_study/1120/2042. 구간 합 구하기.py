import sys

input = sys.stdin.readline


# 세그먼트 트리 만들기
def init(start, end, node):
    # print(start, end, node, tree)
    if start == end:
        tree[node] = numbers[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


# 세그먼트 트리 갱신
def update(start, end, node, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, index, diff)
    update(mid + 1, end, node * 2 + 1, index, diff)


# 구간 합 찾기
def query(start, end, left, right, node):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(start, mid, left, right, node * 2) + query(mid + 1, end, left, right, node * 2 + 1)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    numbers = [int(input()) for _ in range(N)]
    orders = [list(map(int, input().split())) for _ in range(M + K)]

    # 세그먼트 트리 만들기
    tree = [0] * (N * 4)
    init(0, N - 1, 1)
    # print(tree)

    # 갱신 or 값 구하기
    for order in orders:
        command, b, c = order

        if command == 1:
            diff = c - numbers[b - 1]
            numbers[b - 1] = c
            update(0, N - 1, 1, b - 1, diff)
        else:
            print(query(0, N - 1, b - 1, c - 1, 1))
