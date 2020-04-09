class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def add(self, index, data):
        if index >= self.length():
            print("ERROR: 'add' Index out of range!")
            return
        new_node = Node(data)
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = new_node
                new_node.next = cur_node
                return
            cur_idx += 1

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1




T = int(input())

for t in range(1, T + 1):
    my_list = LinkedList()
    n, m, l = map(int, input().split())
    numbers = list(map(int, input().split()))

    for number in numbers:
        my_list.append(number)
    print(my_list.display())
    for i in range(m):
        idx, num = map(int, input().split())
        my_list.add(idx, num)

    print('#{} {}'.format(t, my_list.get(l)))
    print(my_list.display())
