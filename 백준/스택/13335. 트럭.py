from collections import deque


def solution(n, w, L, trucks):
    trucks = deque(trucks)  # 대기중인 트럭
    on_the_bridge = deque()  # 다리위의 트럭
    departure_time_truck = deque()  # 각 트럭이 다리위로 올라간 시간

    time = 0
    while on_the_bridge or trucks:
        time += 1
        if on_the_bridge:
            # 도착시간이 되면 트럭 빼준다
            if departure_time_truck[0] + w == time:
                on_the_bridge.popleft()
                departure_time_truck.popleft()

        if trucks:
            # 트럭이 들어갈 자리가 있으면 트럭을 다리위로 넣어줌
            if sum(on_the_bridge) + trucks[0] <= L:
                on_the_bridge.append(trucks.popleft())
                departure_time_truck.append(time)

    print(time)


if __name__ == "__main__":
    # 다리를 건너는 트럭의 수, 다리의 길이, 다리의 최대하중
    n, w, L = map(int, input().split())
    # 트럭들
    trucks = list(map(int, input().split()))
    solution(n, w, L, trucks)
