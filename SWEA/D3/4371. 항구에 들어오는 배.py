for tc in range(int(input())):
    N = int(input())
    happy_days = []
    for i in range(N):
        happy_days.append(int(input()))

    ships = set()
    answer = 0
    for i in range(1, len(happy_days)):
        if happy_days[i] in ships:
            continue
        gap = happy_days[i] - 1
        for j in range(1 + gap, happy_days[-1] + 1, gap):
            ships.add(j)
        answer += 1

    print(f'#{tc + 1} {answer}')
