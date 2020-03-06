for t in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # print(numbers)

    max_score = sum(numbers)

    score_list = [1] + [0] * max_score

    # print(score_list)

    for score in numbers:
        for i in range(max_score - score, -1, -1):
            if score_list[i] == 1:
                score_list[i + score] = 1

    # print(score_list)
    # print(sum(score_list))

    print('#{} {}'.format(t, sum(score_list)))