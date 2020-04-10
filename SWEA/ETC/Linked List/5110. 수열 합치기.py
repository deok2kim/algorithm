class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def display(self):
        elems = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            elems.append(cur.data)
        # print(elems)
        return elems

    def add(self, index, data):
        new_node = Node(data)
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = new_node
                new_node.next = cur_node
                self.size += 1
                return
            cur_idx += 1

    def merge(self, numbers):
        cur_node = self.head
        cur_idx = 0
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == self.size or cur_node.data > numbers[0]:
                for number in numbers[::-1]:
                    my_list.add(cur_idx, number)
                return
            cur_idx += 1


T = int(input())
for t in range(1, T + 1):
    my_list = LinkedList()
    n, m = map(int, input().split())

    for i in range(m):
        numbers = list(map(int, input().split()))
        if i == 0:
            for number in numbers:
                my_list.append(number)
        else:
            my_list.merge(numbers)

    result = my_list.display()
    result.reverse()
    print('#{} {}'.format(t, ' '.join(list(map(str, result[:10])))))
