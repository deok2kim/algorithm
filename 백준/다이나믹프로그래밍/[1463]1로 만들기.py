def one(n):
    for i in range(2, n+1):
        cnt_list[i] = min(cnt_list[i//3] if i%3==0 else 9999, cnt_list[i//2] if i%2==0 else 9999, cnt_list[i-1]) + 1
    pass


n = int(input())
cnt_list = [0]*(n+1)
one(n)
print(cnt_list[-1])