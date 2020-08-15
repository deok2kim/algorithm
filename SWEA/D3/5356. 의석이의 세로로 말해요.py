T = int(input())
for t in range(1, T + 1):
    words = [list(input()) for _ in range(5)]
    result = ''
    max_len = 0

    for word in words:
        if len(word) > max_len:
            max_len = len(word)

    for i in range(len(words)):
        for j in range(max_len-len(words[i])):
            words[i].append('')


    for i in range(max_len):
        for j in range(len(words)):
            result += words[j][i]

    print('#{} {}'.format(t, result))
