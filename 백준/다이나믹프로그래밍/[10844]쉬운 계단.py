n = int(input())

result = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for i in range(1, n):
    tmp = []
    for j in range(10):
        if j == 0:
            tmp.append(result[-1][1])
        elif j == 9:
            tmp.append(result[-1][8])
        else:
            tmp.append(result[-1][j - 1] + result[-1][j + 1])
    result.append(tmp)

# print(result)
print(sum(result[-1]) % 1000000000)
#
# for i in result:
#     print(sum(i))
