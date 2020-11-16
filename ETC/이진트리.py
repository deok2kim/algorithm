# 노드 만들기
#         A(val)
#        /      \
#   B(left)     C(right)
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


# 이진트리 만들기
class BinaryTree:
    # 초기값 head는 None
    def __init__(self):
        self.head = Node(None)

        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []

    # 값 추가하기 head가 없을 경우
    def add(self, item):
        if self.head.val is None:
            self.head.val = item

        # head가 있으면 왼쪽배치 or 오른쪽배치
        else:
            self.__add_node(self.head, item)

    # head가 있는 경우
    def __add_node(self, cur, item):
        print('부모:', cur.val, '자식:', item)
        # head 값이 크면 왼쪽으로
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        # head 값이 작으면 오른쪽으로
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    # 찾기!!
    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        print(cur.val, item)
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False

    # 지우기!!

    def remove(self, item):
        if self.head.val == item:

            # 자식이 없을 때 - 그냥 지운다
            if self.head.left == None and self.head.right == None:
                self.head.val = None

            # 자식이 하나있을 때 - 부모를 지우고 자식을 할아버지한테 붙인다.
            elif self.head.left == None and self.head.right != None:
                self.head = self.head.right
            elif self.head.left != None and self.head.right == None:
                self.head = self.head.left
            # 자식이 둘 있을 때 - 오른쪽 자식의 가장 왼쪽 자식으로 바꿔준다.
            else:
                self.head.val = self.__remove_right_and_most_left(self.head.right)

        else:
            if self.head.val > item:
                self.__remove(self.head, self.head.left, item)
            else:
                # print(self.head.val, self.head.right.val, item)
                self.__remove(self.head, self.head.right, item)

    def __remove(self, parent, cur, item):
        print(parent.val, cur.val, item)
        if cur is None:
            print('No item', item)
        if cur.val == item:
            # 자식이 없을 때

            if cur.left == None and cur.right == None:
                print('여기오네')
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None

            # 자식이 하나 있을 때 - 부모를 지우고 자식을 할아버지한테 붙인다.
            elif cur.left == None and cur.right != None:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right

            elif cur.left != None and cur.right == None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left

            # 자식이 둘 있을 때 - 오른쪽 자식의 가장 왼쪽 자식으로 바꿔준다.
            if cur.left != None and cur.right != None:
                cur.val = self.__remove_right_and_most_left(cur.right).val
                self.__removeitem(cur, cur.right, cur.val)

        else:
            if cur.val > item:
                self.__remove(cur, cur.left, item)
            else:
                self.__remove(cur, cur.right, item)


    # 오른쪽 자식의 가장 왼쪽 자식 찾기
    def __remove_right_and_most_left(self, cur):
        if cur.left == None:
            return cur
        else:
            return self.__remove_right_and_most_left(cur.left)

    # 자식이 둘일 때 오른쪽 자식의 가장 왼쪽 자식을 옮기고 그 자식은 지우기
    def __removeitem(self, parent, cur, item):
        if cur.val == item:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        else:
            if cur.val > item:
                self.__removeitem(cur, cur.left, item)
            else:
                self.__removeitem(cur, cur.right, item)

    # 순회 Traverse
    # 전위순회 preorder 1. 루트 방문, 2. 왼쪽 서브트리, 3. 오른쪽 서브트리
    # 완성되어 있는 트리를 다른 서버에 리스트 형태로 보내서 그 서버에서 다시 트리를 구성할 때 사용
    def preorder_traverse(self):
        self.preorder_list = []
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        self.preorder_list.append(cur.val)
        # print(cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    # 정위순회 inorder 1. 왼쪽 2. 루트 3. 오른쪽
    # 오름차순 정렬할 때 | n의 시간복잡도로 정렬가능
    def inorder_traverse(self):
        self.inorder_list = []
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        self.inorder_list.append(cur.val)
        # print(cur.val)

        if cur.right is not None:
            self.__inorder(cur.right)

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

        self.postorder_list.append(cur.val)
        # print(cur.val)


lst = [50, 30, 24, 5, 28, 45, 98, 52, 60]
bt = BinaryTree()
for num in lst:
    bt.add(num)

print(bt.search(60))
# 전우
bt.preorder_traverse()
print(bt.preorder_list)
# 중위
bt.inorder_traverse()
print(bt.inorder_list)
# 후위
bt.postorder_traverse()
print(bt.postorder_list)

bt.remove(24)
print(bt.search(60))
# 전우
bt.preorder_traverse()
print(bt.preorder_list)
# 중위
bt.inorder_traverse()
print(bt.inorder_list)
# 후위
bt.postorder_traverse()
print(bt.postorder_list)
# 출처: https://www.youtube.com/watch?v=0CqDdXOr6Kk
