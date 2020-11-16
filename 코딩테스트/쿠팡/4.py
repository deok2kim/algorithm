from collections import defaultdict


def solution(depar, hub, dest, roads):
    answer = -1

    adj = defaultdict(list)
    for road in roads:
        s, e = road
        adj[s].append(e)

    print(adj)

    # depar(출발지) 에서 hub(중간점) 으로 가는 경우의 수
    hub_cnt = 0
    stack = []
    stack.append(depar)
    while stack:
        c = stack.pop()
        for neighbor in adj[c]:
            if neighbor == hub:
                hub_cnt += 1
            else:
                stack.append(neighbor)

    # hub에서 dest(도착지) 로 가는 경우의 수
    dest_cnt = 0
    stack = []
    stack.append(hub)
    while stack:
        c = stack.pop()
        for neighbor in adj[c]:
            if neighbor == dest:
                dest_cnt += 1
            else:
                stack.append(neighbor)

    result = hub_cnt * dest_cnt
    if result:
        answer = result
    else:
        answer = 0
    return answer


print(solution("SEOUL", "DAEGU", "YEOSU",
               [["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "DAEJEON"],
                ["SEOUL", "ULSAN"], ["DAEJEON", "DAEGU"], ["GWANGJU", "BUSAN"], ["DAEGU", "GWANGJU"],
                ["DAEGU", "BUSAN"], ["ULSAN", "DAEGU"], ["GWANGJU", "YEOSU"], ["BUSAN", "YEOSU"]]))
print(solution("ULSAN", "SEOUL", "BUSAN",
               [["SEOUL", "DAEJEON"], ["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"],
                ["SEOUL", "ULSAN"], ["DAEJEON", "BUSAN"], ["GWANGJU", "BUSAN"]]))
