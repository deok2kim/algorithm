from collections import defaultdict


def solution(tickets):
    answer = []
    adj = defaultdict(list)

    for ticket in tickets:
        adj[ticket[0]].append(ticket[1])

    for key in adj.keys():
        adj[key].sort(reverse=True)

    q = ['ICN']
    while q:
        tmp = q[-1]

        if not adj[tmp]:
            answer.append(q.pop())
        else:
            q.append(adj[tmp].pop())
    answer.reverse()
    return answer


print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
print(solution([['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]))
print(solution([['ICN', '1'], ['1', '2'], ['1', '3'], ['3', '1']]))
print(solution([['ICN', '1'], ['1', 'ICN'], ['1', 'a'], ['ICN', '1']]))
print(solution([['ICN', 'A'], ['A', 'B'], ['A', 'C'], ['C', 'A'], ['B', 'D']]))
