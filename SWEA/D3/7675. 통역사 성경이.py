for tc in range(int(input())):
    N = int(input())
    answer = list()
    sentence = input()

    # 문장 구분하기
    start = 0
    for i in range(len(sentence)):
        if sentence[i] in ('!', '?', '.'):
            # 단어로 구분하기
            cnt = 0
            for word in sentence[start:i].split():
                # 이름인지 판별하기
                if (len(word) == 1 and word[0].isupper()) or (
                        word[0].isupper() and word.isalpha() and word[1:].islower()):
                    cnt += 1
            start = i + 2

            answer.append(cnt)

    print(f'#{tc + 1}', *answer)
