from _collections import deque


def solution(cacheSize, cities):
    answer = 0

    q = deque()

    # cache = collections.deque(maxlen=cacheSize)
    # maxlen 을 설정해주면 q의 길이기 cachesize를 넘기는 경우를 고려하지 않아도 된다.
    for city in cities:
        city = city.lower()
        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        else:
            q.append(city)
            if len(q) > cacheSize:
                q.popleft()
            answer += 5

    return answer


print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(2, ['Jeju', 'Pangyo', 'NewYork', 'newyork']))
print(solution(2, ['jeju', 'jeju']))
