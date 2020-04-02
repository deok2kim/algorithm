T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza_idx = [x for x in range(1,m+1)]
    q = []
    idx = []

    for i in range(n):
        q.append(pizza.pop(0))
        idx.append(pizza_idx.pop(0))

    while len(q) > 1:
        if len(q) != n and pizza:
            q.append(pizza.pop(0))
            idx.append(pizza_idx.pop(0))

        else:
            a = q.pop(0)
            i = idx.pop(0)
            if a // 2 != 0:
                q.append(a//2)
                idx.append(i)
    # print(q)
    # print(idx)
    print('#{} {}'.format(t, idx[0]))
