class Node:
    """연결 리스트용 노드 클래스"""

    def __init__(self, data=None, next=None):
        """초기화"""
        self.data = data
        self.next = next


class LinkedList:
    """연결 리스트 클래스"""

    def __init__(self):
        self.no = 0  # 노드의 개수
        self.head = None  # 머리 노드
        self.current = None  # 주목 노드

    def add_first(self, data):
        """맨 앞에 노드를 삽입"""
        ptr = self.head  # 삽입하기 전의 머리 노드
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data):
        """맨 뒤에 노드를 삽입"""
        if self.head is None:  # 리스트가 비어있는 경우
            self.add_first(data)  # 맨 앞에 노드를 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data)
            # ptr.next = self.current = Node(data, None)  # default 값이 None 이므로 안써줘도 된다.
            self.no += 1

    def remove_first(self):
        """머리 노드 삭제"""
        if self.head is not None:  # 리스트가 비어있지 않으면 다음 노드를 헤드로 변경
            self.head = self.current = self.head.next
            self.no -= 1

    def remove_last(self):
        """꼬리 노드 삭제"""
        if self.head is not None:  # 리스트가 비어있지 않으면
            if self.head.next is None:  # 노드가 1개일 때
                self.remove_first()
            else:
                ptr = self.head  # 스캔 중인 노드
                pre = self.head  # 스캔 중인 노드의 앞쪽 노드
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next

                pre.next = None  # 꼬리 노드 삭제
                self.current = pre
                self.no -= 1

    def remove(self, p):
        """노드 p를 삭제"""
        if self.head is not None:  # 리스타가 비어있지 않으면
            ptr = self.head

            while ptr.next is not p:  # p 노드를 찾을 때까지 진행
                ptr = ptr.next

            ptr.next = p.next  # ptr 다음 p 다음 p.next 이지만 p 를 건너 뛰고
            self.current = ptr
            self.no -= 1

    def remove_current_node(self):
        """주목 노드(currnet)를 삭제"""
        self.remove(self.current)

    def clear(self):
        """전체 노드를 삭제"""
        while self.head is not None:  # 리스트가 비어있을 때까지
            self.remove_first()  # 머리 노드를 삭제

        self.current = None
        self.no = 0

    def next(self):
        """주목 노드를 한 칸 뒤로 이동"""
        if self.current is None or self.current.next is None:  # 주목 노드가 None 이거나 다음 노드가 없으면
            return False  # 이동 불가
        else:
            self.current = self.current.next
            return True

    def print_current_node(self):
        """주목 노드를 출력"""
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    def print(self):
        """모든 노드를 출력"""
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=' ')
            ptr = ptr.next

    def search(self, data):
        """data의 값을 검색"""
        ptr = self.head
        cnt = 0
        while ptr is not None:
            if ptr.data == data:
                return cnt
            cnt += 1
            ptr = ptr.next
        else:
            return -1  # 못 찾은 경우

    def __contains__(self, data):
        """data가 포함되어 있는지 확인"""
        return self.search(data) >= 0

    def __iter__(self):
        return LinkedListIterator(self.head)


class LinkedListIterator:
    """클래스 LinkedList의 이터레이터용 클래스"""

    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


# 객체 생성
lst = LinkedList()
print()
# 값 넣기
lst.add_first(3)
lst.add_first(2)
lst.add_first(1)
lst.add_last(6)
lst.add_last(5)
lst.add_last(4)
print()
# 값 찾기
print(lst.search(1))
print(lst.search(2))
print(lst.search(3))
print(lst.search(4))
print(lst.search(5))
print(lst.search(6))
print(lst.search(10))
print()
# 주목 노드 출력
lst.print_current_node()
print()
# 모든 노드 출력
lst.print()

# 이터레이터
arr = lst.__iter__()
for i in arr:
    print(i)
