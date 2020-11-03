def find_block(x: int) -> int:
    # 오른쪽으로 가면서 자신보다 크거나 같은 블럭을 찾는다.
    # 가는 중에 자신보다 작지만 그 중에 가장 큰 놈을 찜해 놓는다.
    max_block = [0, 0]
    for j in range(x + 1, W):
        if block[j] >= block[x]:
            return j

        if max_block[1] <= block[j]:
            max_block[1] = block[j]
            max_block[0] = j

    return max_block[0]


def fill_rainwater(x: int, y: int) -> int:
    # 자신보다 같거나 큰놈이 없으면 찜해놓은 녀석의 높이만큰 물을 채운다.
    # 자신보다 같거나 큰놈이 있으면 자신의 높이만큼 물을 채운다.
    rainwater = min(block[x], block[y])
    cnt = 0
    for j in range(x + 1, y):
        cnt += rainwater - block[j]
        block[j] = rainwater

    return cnt


if __name__ == '__main__':
    H, W = map(int, input().split())  # 세로 가로
    block = list(map(int, input().split()))
    answer = 0

    i = 0
    while i < W - 1:
        b = find_block(i)
        answer += fill_rainwater(i, b)
        i = b
    print(answer)
