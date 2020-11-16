from itertools import chain


def solution(arr):
    answer = []
    a = 0
    b = 0
    for row in arr:
        print(row)
    print()

    def compression(lst):
        nonlocal a, b
        length = len(lst) // 2
        print(length)
        # 왼쪽 위

        llst = lst[:length]
        for i in range(length):
            llst[i] = llst[i][:length]
        sum_llst = sum(list(map(int, chain.from_iterable(llst))))
        if sum_llst == length ** 2:
            b += 1
        elif sum_llst == 0:
            a += 1
        else:
            compression(llst)

        # 오른쪽 위
        llst = lst[:length]
        for i in range(length):
            llst[i] = llst[i][length:]
        sum_llst = sum(list(map(int, chain.from_iterable(llst))))
        if sum_llst == length ** 2:
            b += 1
        elif sum_llst == 0:
            a += 1
        else:
            compression(llst)
        # 왼쪽 아래
        llst = lst[length:]
        for i in range(length):
            llst[i] = llst[i][:length]
        sum_llst = sum(list(map(int, chain.from_iterable(llst))))
        if sum_llst == length ** 2:
            b += 1
        elif sum_llst == 0:
            a += 1
        else:
            compression(llst)

        # 오른쪽 아래
        llst = lst[length:]
        for i in range(length):
            llst[i] = llst[i][length:]
        sum_llst = sum(list(map(int, chain.from_iterable(llst))))
        if sum_llst == length ** 2:
            b += 1
        elif sum_llst == 0:
            a += 1
        else:
            compression(llst)

    compression(arr)
    print(a, b)
    answer = [a,b]
    return answer


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
