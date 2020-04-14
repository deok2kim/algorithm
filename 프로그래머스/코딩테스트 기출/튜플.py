def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    numbers_list = []

    for i in s:
        tmp = list(map(int, i.split(',')))
        numbers_list.append(tmp)

    numbers_list.sort(key=len)

    for numbers in numbers_list:
        for j in numbers:
            if j not in answer:
                answer.append(j)

    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
