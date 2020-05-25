def bf():
    for i in range(len(eureka)):
        for j in range(len(eureka)):
            for k in range(len(eureka)):
                sum = eureka[i] + eureka[j] + eureka[k]
                if sum == N:
                    return 1

    else:
        return 0


eureka = [1]
cnt = 2
for tc in range(1, int(input())+1):
    N = int(input())

    while True:
        n = eureka[-1]
        if n > 1000:
            break

        n = n + cnt
        cnt += 1
        eureka.append(n)

    print(bf())