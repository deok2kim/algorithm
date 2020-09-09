def solution(dartResult):
    answer = 0

    my_results = []
    i = 0
    for j in range(1, len(dartResult)):
        if dartResult[j].isdigit() and j - i != 1:
            my_results.append(dartResult[i:j])
            i = j

    else:
        my_results.append(dartResult[i:])
    print(my_results)

    scores = []
    for i, result in enumerate(my_results):
        for j in range(len(result)):
            if result[j].isalpha():
                s = int(result[:j])
                multi = result[j]
                break

        print(s)

        if multi == 'S':
            score = s ** 1
        elif multi == 'D':
            score = s ** 2
        elif multi == 'T':
            score = s ** 3

        scores.append(score)
        if len(result) == 3:
            prize = result[2]

            if prize == '*':
                if i > 0:
                    scores[i] *= 2
                    scores[i - 1] *= 2
                else:
                    scores[i] *= 2
            elif prize == '#':
                scores[i] *= -1

        # print(scores)

    answer += sum(scores)
    return answer


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S2D*3T"))
