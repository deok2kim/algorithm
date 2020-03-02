def solution(arr):
    answer = 1

    total = []
    number_dict = {}
    for num in arr:
        tmp = []

        while num >= 2:

            for i in range(2, num + 1):
                if num % i == 0:
                    num = num // i
                    tmp.append(i)
                    break

        ttmp = set(tmp)
        for j in ttmp:
            cnt = tmp.count(j)
            if number_dict.get(j) is None:
                number_dict[j] = cnt
            else:
                if number_dict[j] < cnt:
                    number_dict[j] = cnt


    print(number_dict)
    for key, value in number_dict.items():
        answer *= key**value
    return answer

print(solution([2,6,8,14]))
print(solution([1,2,3]))