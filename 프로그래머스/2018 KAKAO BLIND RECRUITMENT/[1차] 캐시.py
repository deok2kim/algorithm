from collections import deque


def solution(cacheSize, cities):
    answer = 0
    memory = deque()
    if cacheSize == 0:
        return len(cities) * 5

    for i in range(len(cities)):
        # print(memory, answer, cities[i])
        city = cities[i].upper()
        if len(memory) < cacheSize:
            if city in memory:
                answer += 1
                memory.remove(city)
                memory.append(city)
            else:
                answer += 5
                memory.append(city)
        elif len(memory) == cacheSize:
            if city in memory:
                answer += 1
                memory.remove(city)
                memory.append(city)
            else:
                answer += 5
                memory.popleft()
                memory.append(city)
    # print(memory)
    return answer


print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(2,
               ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork',
                'Rome']))
print(solution(5,
               ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork',
                'Rome']))
print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(1, ['A', 'A', 'b', 'A', 'A', 'A', 'b']))
