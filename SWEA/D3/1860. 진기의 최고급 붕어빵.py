T = int(input())

for t in range(1, T+1):
    n, m, k = map(int, input().split())  # n명, m초 마다 k개씩 생산
    people = list(map(int, input().split()))
    people.sort()
    result = 'Possible'
    for i in range(len(people)):
        if people[i]//m * k > i + 1:
            result = 'Impossible'
            break

    print('#{} {}'.format(t, result))
