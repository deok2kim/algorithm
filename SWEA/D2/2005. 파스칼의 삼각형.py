T = int(input())

for t in range(1, T + 1):
    n = int(input())
    result = [[1]]
    for i in range(1, n):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(result[i-1][j-1] + result[i-1][j])
        result.append(tmp)
    print('#{}'.format(t))
    for i in result:
        print(' '.join(list(map(str, i))))
