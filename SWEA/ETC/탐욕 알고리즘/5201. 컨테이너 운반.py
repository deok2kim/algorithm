for tc in range(int(input())):
    n, m = map(int, input().split())  # 컨테이너 수, 트럭 수
    weights = list(map(int, input().split()))
    capacities = list(map(int, input().split()))

    weights.sort(reverse=True)
    capacities.sort(reverse=True)

    result = 0
    truck = 0
    for i in range(len(weights)):
        if capacities[truck] >= weights[i]:
            result += weights[i]
            truck += 1

        if truck == len(capacities):
            break

    print('#{} {}'.format(tc+1, result))
    