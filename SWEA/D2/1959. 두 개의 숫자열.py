T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())

    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    if n > m:
        lst1, lst2, n, m = lst2, lst1, m, n

    result = []
    for i in range(m-n+1):
        tot = 0
        for j in range(n):
            tot += lst1[j]*lst2[i+j]

        result.append(tot)

    print('#{} {}'.format(t, max(result)))
