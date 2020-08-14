keypad = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

for tc in range(1, 1 + int(input())):
    s, n = input().split()
    words = input().split()

    cnt = 0
    for word in words:
        for i in range(len(word)):
            if word[i] not in keypad[s[i]]:
                break
        else:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
