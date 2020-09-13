import sys

sys.setrecursionlimit(10 ** 9)


class Node:
    def __init__(self, item, id):
        self.val = item
        self.left = None
        self.right = None
        self.id = id


class BinaryTree:
    # 초기값 head는 None
    def __init__(self):
        self.head = Node(None, None)

        self.preorder_list = []
        self.postorder_list = []

    # 값 추가하기 head가 없을 경우
    def add(self, item, id):
        if self.head.val is None:
            self.head.val = item
            self.head.id = id

        # head가 있으면 왼쪽배치 or 오른쪽배치
        else:
            self.__add_node(self.head, item, id)

    # head가 있는 경우
    def __add_node(self, cur, item, id):
        # print('부모:', cur.val, '자식:', item, 'id: ',id)
        # head 값이 크면 왼쪽으로
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item, id)
            else:
                cur.left = Node(item, id)
        # head 값이 작으면 오른쪽으로
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item, id)
            else:
                cur.right = Node(item, id)

    def preorder_traverse(self):
        self.preorder_list = []
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        self.preorder_list.append(cur.id)
        # print(cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    # 후위순회 postorder 1. 왼쪽, 3. 오른쪽, 3. 루트
    #
    def postorder_traverse(self):
        self.postorder_list = []
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)

        if cur.right is not None:
            self.__postorder(cur.right)

        self.postorder_list.append(cur.id)
        # print(cur.val)


def solution(nodeinfo):
    answer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo.sort(key=lambda x: -x[1])
    # print(nodeinfo)
    bt = BinaryTree()
    for i in range(len(nodeinfo)):
        bt.add(nodeinfo[i][0], nodeinfo[i][2])
    bt.preorder_traverse()
    bt.postorder_traverse()
    # print(bt.preorder_list)
    # print(bt.postorder_list)
    answer.append(bt.preorder_list)
    answer.append(bt.postorder_list)

    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
