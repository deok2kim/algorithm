from typing import Any


class Stack:
    class Empty(Exception):
        """스택이 비어있을 때 pop 또는 peek 를 수행할 때 예외 처리"""
        print("야")
        pass

    class Full(Exception):
        """스택이 가득일 때 push 를 수행할 때 예외 처리"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """스택 초기화"""
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수 반환"""
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어 있는지"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택이 가득차 있는지"""
        return self.ptr >= self.capacity

    def push(self, item: Any) -> None:
        """스택에 데이터를 쌓음"""
        if not self.is_full():
            self.stk[self.ptr] = item
            self.ptr += 1
        else:
            raise Stack.Full

    def pop(self) -> Any:
        """스택에서 데이터를 꺼냄"""
        if not self.is_empty():
            self.ptr -= 1
            return self.stk[self.ptr]
        else:
            raise Stack.Empty

    def peek(self) -> Any:
        """스택의 꼭데이에 있는 데이터를 확인"""
        if not self.is_empty():
            return self.stk[self.ptr - 1]
        else:
            raise Stack.Empty

    def clear(self) -> None:
        """스택을 비움"""
        self.ptr = 0

    def find(self, item: Any) -> int:
        """스택에 특정 데이터를 찾아 인덱스 반환"""
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기부터 아래로 선형 검색
            if self.stk[i] == item:
                return i  # 검색 성공
        else:
            return -1  # 검색 실패

    def count(self, item: Any) -> int:
        """스택에 특정 데이터의 개수를 반환"""
        cnt = 0
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == item:
                cnt += 1
        return cnt

    def __contains__(self, item: Any) -> bool:
        """스택에 특정 값이 있는지"""
        return self.find(item) >= 0

    def dump(self) -> None:
        """스택안의 모든 데이터를 바닥부터 꼭대기까지 출력"""
        if self.is_empty():
            print('스택이 비어있습니다.')
        else:
            print(self.stk[:self.ptr])


stack = Stack(10)
stack.dump()
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()
stack.push(8)
stack.push(8)
stack.push(9)
stack.dump()
print(stack.find(8))
print(stack.count(8))
print(stack.__contains__(8))
stack.dump()
