# def dfs(n):
#     global count
#     if n == number:
#         count += 1
#         return
#     elif n > number:
#         return
#
#     else:
#         dfs(n+1)
#         dfs(n+2)
#         dfs(n+3)

def dp(n):
    for i in range(4, n+1):
        if d[i] > 0:
            continue
        else:
            d[i] = d[i-3] + d[i-2] + d[i-1]
    pass

d = [0]*11
d[1] = 1
d[2] = 2
d[3] = 4
for tc in range(int(input())):
    number = int(input())
    count = 0
    dp(number)
    print(d[number])
    print(d)