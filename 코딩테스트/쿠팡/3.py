from collections import defaultdict


def solution(k, score):
    answer = -1
    results = []
    for i in range(len(score) - 1):
        results.append(abs(score[i] - score[i + 1]))
    print(results)

    # 점수차이 같은거 갯수 세기
    count = defaultdict(int)
    for result in results:
        count[result] += 1

    print(count)

    # 빼줄 점수 셋
    score_set = set()
    for c in count:
        if count[c] >= k:
            score_set.add(c)

    print(score_set)

    # 뺀사람들 안뺀사람들
    # 빼면 0이 된다
    people = [1] * (len(score))
    for i in range(len(results)):
        if results[i] in score_set:  # 빼준다
            # 나와 내 뒷놈을 뺀다(0으로 만든다)
            people[i], people[i + 1] = 0, 0
    print(people)

    # 남은 사람은 1인 애들
    answer = sum(people)
    return answer


print(solution(3, [24, 22, 20, 10, 5, 3, 2, 1]))
print(solution(2, [1300000000, 700000000, 668239490, 618239490, 568239490, 568239486, 518239486, 157658638, 157658634,
                   100000000, 100]))
