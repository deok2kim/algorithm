import heapq


def solution(N, logs):
    heapq.heapify(logs)
    my_logs = [0] * N
    left = 0
    right = -1
    for _ in range(N // 2):
        my_logs[left] = heapq.heappop(logs)
        my_logs[right] = heapq.heappop(logs)
        left += 1
        right -= 1
    if logs:
        my_logs[left] = heapq.heappop(logs)

    # 각 통나무들의 차이 구하기
    answer = 0
    for i in range(N):
        answer = max(answer, abs(my_logs[i] - my_logs[i - 1]))
    print(answer)


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        N0 = int(input())  # 통나무 개수
        logs0 = list(map(int, input().split()))
        solution(N0, logs0)
