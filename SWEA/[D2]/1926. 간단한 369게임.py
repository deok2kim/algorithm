n = int(input())

result = []
for i in range(1, n+1):
    cnt = 0
    tmp = list(str(i))
    for j in tmp:
        if j == '3' or j == '6' or j == '9':
            cnt += 1

    if cnt == 0:
        result.append(str(i))
    else:
        result.append('-'*cnt)


print(' '.join(result))