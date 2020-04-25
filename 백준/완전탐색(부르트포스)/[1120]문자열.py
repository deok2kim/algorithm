a, b = input().split()

min_result = 50
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1

    if cnt < min_result:
        min_result = cnt

print(min_result)
