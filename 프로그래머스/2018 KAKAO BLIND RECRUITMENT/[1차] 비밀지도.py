def ez(num, n):
    numbers = []
    while num > 1:
        nmg = num % 2
        num = num // 2
        numbers.append(nmg)
    if num == 0:
        numbers.append(0)
    else:
        numbers.append(1)
    if len(numbers) < n:
        numbers += [0 for _ in range(n - len(numbers))]
    numbers.reverse()
    return numbers


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = ez(arr1[i], n)
        arr2[i] = ez(arr2[i], n)

    for i in range(n):
        tmp = ''
        for j in range(n):
            if arr1[i][j] == 1 or arr2[i][j] == 1:
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(1, [0], [0]))

