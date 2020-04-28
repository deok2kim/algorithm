def backtracking(idx=0):
    if len(result) == 6:
        print(' '.join(list(map(str, result))))
        return
    for i in range(idx, n):
        result.append(numbers[i])
        backtracking(i+1)
        result.remove(numbers[i])

    return

n = -1
while n != 0:
    numbers = list(map(int, input().split()))
    n = numbers.pop(0)
    result = []
    backtracking()
    print()
