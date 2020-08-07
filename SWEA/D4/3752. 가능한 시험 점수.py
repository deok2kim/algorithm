for tc in range(1, 1 + int(input())):
    n = int(input())
    scores = list(map(int, input().split()))

    # 내가 가능한 최대 점수까지 리스트를 만들어준다
    # 인덱스가 내가 얻을 수 있는 점수
    # 1이면 이미 얻을 수 있고, 0이면 얻지 못한다
    my_scores = [0] * (sum(scores) + 1)
    my_scores[0] = 1  # 0점은 가능하니까 바로 1

    # 점수를 하나하나씩 꺼내서
    for score in scores:
        # 만들어둔 리스트의 뒤에서부터 앞으로 하나씩 본다
        for i in range(len(my_scores) - score, -1, -1):
            # 이미 내가 가능한 점수가 내점수 리스트에 있으면
            if my_scores[i]:
                # 그 점수에 방금 얻은 점수를 더해서 그 점수에 해당하는 인덱스를 1로 만든다.
                my_scores[i + score] = 1

    print('#{} {}'.format(tc, sum(my_scores)))
