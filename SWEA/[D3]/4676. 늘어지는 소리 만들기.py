T = int(input())
for t in range(1, T + 1):
    word = input()
    hyphen = int(input())
    idx = [0]*(len(word) + 1)
    for i in list(map(int, input().split())):
        idx[i] += 1
    result = ""
    for i in range(len(idx)):
        result += '-'*idx[i]
        if i < len(word):
            result += word[i]

    print('#{} {}'.format(t, result))
