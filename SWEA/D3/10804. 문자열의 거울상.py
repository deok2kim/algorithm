for tc in range(int(input())):
    word = input()

    answer = ''
    for i in range(len(word) - 1, -1, -1):
        if word[i] == 'b':
            answer += 'd'
        elif word[i] == 'd':
            answer += 'b'
        elif word[i] == 'p':
            answer += 'q'
        else:
            answer += 'p'

    print(f'#{tc + 1} {answer}')
