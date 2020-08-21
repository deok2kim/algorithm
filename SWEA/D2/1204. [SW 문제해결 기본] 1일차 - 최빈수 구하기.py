for tc in range(1, 1+int(input())):
    tt = int(input())
    score = list(map(int, input().split()))
    scores = [0]*101
    for s in score:
        scores[s] += 1

    maxNum = max(scores)
    answer = 0
    for i in range(101):
        if maxNum == scores[i]:
            answer = i

    print('#{} {}'.format(tc, answer))
