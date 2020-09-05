import heapq


def solution(operations):
    answer = []
    for operation in operations:
        order, num = operation.split()
        if order == 'I':
            answer.append(int(num))

        elif order == 'D' and answer:
            if num == '1':
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]


print(solution(['I 7', 'I 5', 'I -5', 'D -1']))
print(solution(['I 16', 'D 1']))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
