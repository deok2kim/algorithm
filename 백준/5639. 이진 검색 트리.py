import sys
sys.setrecursionlimit(1000000)


def postorder(start, end):
    if start > end:  # 종료 조건
        return

    div = end + 1 # 자르기
    for i in range(start + 1, end + 1):
        if preorder_list[start] < preorder_list[i]:
            div = i
            break

    postorder(start + 1, div - 1)  # 왼쪽 서브트리
    postorder(div, end)  # 오른쪽 서브트리
    print(preorder_list[start])


if __name__ == "__main__":
    preorder_list = []
    while True:
        try:
            preorder_list.append(int(sys.stdin.readline()))
        except:
            break

    postorder(0, len(preorder_list) - 1)
