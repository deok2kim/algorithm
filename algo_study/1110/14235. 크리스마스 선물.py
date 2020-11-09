import heapq

if __name__ == '__main__':
    N = int(input())
    pq = []  # 선물을 담을 리스트 ( 우선순위 큐 )
    for _ in range(N):
        input_value = input()
        if input_value == '0':  # 인풋값이 0일 때
            if pq:  # 선물이 있으면 선물
                print(-heapq.heappop(pq))
            else:  # 선물이 없으면 -1
                print(-1)

        else:
            # 거점에서 선물 충전
            present_list = list(map(int, input_value.split()))
            for i in range(1, present_list[0] + 1):
                heapq.heappush(pq, -present_list[i])
