def bt(init, start, end, cost):
    # print(visited)
    global answer
    if len(visited) == n:
        # print(init, start, end, cost + cost_list[end][init])
        if cost_list[end][init]:
            answer = min(answer, cost + cost_list[end][init])
        # print('가격', cost + cost_list[end][init])
        return

    if cost >= answer:
        return

    for k in range(n):
        if k not in visited and cost_list[end][k]:
            visited.add(k)
            # print(k)
            bt(init, end, k, cost + cost_list[end][k])
            visited.remove(k)


n = int(input())
cost_list = [list(map(int, input().split())) for _ in range(n)]
# for row in cost_list:
#     print(row)
# print()

answer = float('inf')
visited = set()
for i in range(n):
    visited.add(i)
    bt(i, i, i, cost_list[i][i])
    visited.remove(i)

print(answer)
