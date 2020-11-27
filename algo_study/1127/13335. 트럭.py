from _collections import deque

if __name__ == '__main__':
    n, w, L = map(int, input().split())  # 트럭 수, 다리의 길이, 최대 하중
    truck_list = deque(list(map(int, input().split())))

    on_the_bridge = deque()
    on_the_bridge_time = deque()
    time = 0

    while truck_list or on_the_bridge:
        time += 1
        # 트럭이 다리위에 있으면 빼고 넣기
        if on_the_bridge:
            if on_the_bridge_time[0] + w == time:
                on_the_bridge.popleft()
                on_the_bridge_time.popleft()

        # 트럭 넣기
        if truck_list and sum(on_the_bridge) <= L - truck_list[0]:
            on_the_bridge.append(truck_list.popleft())
            on_the_bridge_time.append(time)

    print(time)
