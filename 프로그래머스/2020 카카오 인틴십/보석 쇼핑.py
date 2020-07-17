def solution(gems):
    answer = []


    n_gems = len(set(gems))  # 보석 종류의 갯수

    start, end = 0, 0  # 시작점과 끝점
    get_gems = {gems[0]:1}  # start와 end사이의 보석의 종류에 따른 갯수
    answer = [0, len(gems)]  # 최소길이 반환을 위해 저장할 변수

    while start < len(gems) and end < len(gems):
        if len(get_gems) == n_gems:  # start 와 end 사이에 보석의 종류가 전부 하나씩 존재할 경우
            if end-start < answer[1]-answer[0]:  # 최소 길이 비교
                answer = [start+1, end+1]

            if get_gems.get(gems[start]):  # start 에 있는 보석은 빼주고
                get_gems[gems[start]] -= 1

            if get_gems[gems[start]] == 0:  # 그 보석이 0개가 되면 제거해준다.
                del get_gems[gems[start]]

            start += 1  # 시작점을 +1 해준다.

        else:  # start 와 end 사이에 보석의 종류가 전부가 아닐 경우
            end += 1  # 끝점을 +1 해주고

            if end == len(gems):  # 끝점이 인덱스를 벗어날 수 있으므로 조건문을 걸어준다.
                break

            if get_gems.get(gems[end]):  # 보석이 이미 있으면 +1
                get_gems[gems[end]] += 1

            else:
                get_gems[gems[end]] = 1  # 없으면 새로만들어 1로 설정

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]	))
print(solution(["XYZ", "XYZ", "XYZ"]	))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	))