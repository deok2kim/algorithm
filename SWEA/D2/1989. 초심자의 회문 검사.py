T = int(input())
for t in range(1, T + 1):

    result = 0
    word = input()
    len_word = len(word) // 2

    a = list(word[:len_word])
    b = list(word[-len_word:])
    b.reverse()

    print(a, b)
    if a == b:
        result = 1

    print('#{} {}'.format(t, result))