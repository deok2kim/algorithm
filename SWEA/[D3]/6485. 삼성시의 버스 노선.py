for tc in range(1, 1+int(input())):
    N = int(input())

    # 버스 정류장 배열
    bus_stop = [0]*5001

    # 각각의 정류장에 대하여 +1씩 더해준다.
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            bus_stop[i] += 1

    P = int(input())
    answer = []

    # 구하고자 하는 정류장의 값을 답에 넣어준다.
    for i in range(P):
        p = int(input())
        answer.append(bus_stop[p])
    print('#{} {}'.format(tc, ' '.join(list(map(str, answer)))))

