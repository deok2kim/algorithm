# 인풋
T = int(input())
Ns = [int(input()) for _ in range(T)]

# 풀이
results = []
for tc in range(T):
    n = Ns[tc]
    result = []
    # 전체: n(n+1)//2
    result.append(n*(n+1)//2)
    # 홀수: n**2
    result.append(n**2)
    # 짝수: n(n+1)
    result.append(n*(n+1))


    results.append(result)
# 결과
for tc in range(T):
    print(f'#{tc+1}', end=" ")
    print(*results[tc])
