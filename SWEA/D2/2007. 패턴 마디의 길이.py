T = int(input())

for t in range(1, T + 1):
    words = input()
    answer = 0
    for i in range(1, len(words)//2+1):
        result = []
        # print()
        # print('단어', words[:i])
        repet = words[:i]
        for j in range(0, len(words), i):
            tmp = words[j:j+i]
            if len(tmp) == len(repet) :
                result.append(tmp)

        if len(set(result)) == 1:
            answer = len(repet)
            break

    print('#{} {}'.format(t, answer))