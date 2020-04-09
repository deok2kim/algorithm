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
            # print("ERROR: 'add' Index out of range!")
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

    def erase(self, index):
        if index >= self.length():
            # print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def change(self, index, data):
        if index >= self.length():
            print("ERROR: 'Change' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            # print(cur_idx, cur_node)
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                cur_node.data = data
                last_node.next = cur_node
                return
            cur_idx += 1

    def get(self, index):
        if index >= self.length():
            # print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


T = int(input())

for t in range(1, T + 1):
    my_list = LinkedList()
    n, m, l = map(int, input().split())
    numbers = list(map(int, input().split()))

    for number in numbers:
        my_list.append(number)

    for i in range(m):
        mission = input().split()
        if mission[0] == 'I':
            my_list.add(int(mission[1]), int(mission[2]))
        elif mission[0] == 'D':
            my_list.erase((int(mission[1])))
        elif mission[0] == 'C':
            my_list.change(int(mission[1]), int(mission[2]))
        # my_list.display()

    result = my_list.get(l)
    if result is None:
        result = -1
    print('#{} {}'.format(t, result))
