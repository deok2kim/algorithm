T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    students = list(map(int, input().split()))
    result = list(range(1, n + 1))
    for student in students:
        result.remove(student)

    print('#{} {}'.format(t, ' '.join(list(map(str, result)))))
