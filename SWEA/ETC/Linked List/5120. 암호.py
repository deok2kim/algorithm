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

    def specialAdd(self, index):
        cur_idx = 0
        cur_node = self.head
        first_node = cur_node.next
        # print('first', 'last', 'cur')
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            # print(first_node.data, last_node.data, cur_idx)

            if cur_idx == index:
                if index != self.size:
                    new_node = Node(last_node.data + cur_node.data)
                    last_node.next = new_node
                    new_node.next = cur_node
                    self.size += 1
                    return
                else:
                    new_node = Node(last_node.data + first_node.data)
                    last_node.next = new_node
                    self.size += 1
                    return
            cur_idx += 1


T = int(input())
for t in range(1, T + 1):
    my_list = LinkedList()
    n, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    for number in numbers:
        my_list.append(number)

    idx = 0
    for i in range(k):
        idx += m
        if idx > my_list.size:
            idx = idx % my_list.size
        # print('idx', idx, 'size', my_list.size)
        my_list.specialAdd(idx)
        # print(my_list.display())
    result = my_list.display()
    result.reverse()
    if len(result) > 10:
        result = result[:10]

    print('#{} {}'.format(t, ' '.join(list(map(str, result)))))
