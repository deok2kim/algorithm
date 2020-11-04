import sys
import heapq

input = sys.stdin.readline


def push_heap(left_heap: list, right_heap: list, num: int, n: int):
    # 숫자의 개수가 홀수이면 오른쪽에 넣고, 짝수면 왼쪽에 넣기
    if n % 2 == 1:
        heapq.heappush(right_heap, num)
    else:
        heapq.heappush(left_heap, -num)


def make_mid_heap(left_heap: list, right_heap: list):
    # 레프트의 최대값이 라이트의 최소값보다 크면 위치 교환
    if left_heap:  # 라이트만 있을 수 있기 때문에 if문 처리
        left_max = -left_heap[0]
        right_min = right_heap[0]
        if left_max > right_min:
            heapq.heappush(left_heap, -heapq.heappop(right_heap))
            heapq.heappush(right_heap, -heapq.heappop(left_heap))


def get_mid_number(left_heap: list, right_heap: list, n: int) -> int:
    # 숫자의 개수가 홀수이면, 라이트에서 최소값을 반환
    # 숫자의 개수가 짝수이면, 레프트 최대와 라이트 최소를 비교하여 최소값 반환
    if n % 2 == 1:
        return right_heap[0]
    else:
        return min(-left_heap[0], right_heap[0])


if __name__ == '__main__':
    N = int(input())  # 숫자의 개수
    left_numbers = []  # 최대 힙(최대값을 음수로 넣어 최대값이 0번에 오게 한다)
    right_numbers = []  # 최소 힙

    for i in range(1, N + 1):
        number = int(input())
        push_heap(left_numbers, right_numbers, number, i)
        make_mid_heap(left_numbers, right_numbers)
        answer = get_mid_number(left_numbers, right_numbers, i)
        print(answer)
