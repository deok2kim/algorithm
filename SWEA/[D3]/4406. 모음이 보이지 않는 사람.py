T = int(input())
for t in range(1, T + 1):
    word = input()
    vowel = 'aeiou'

    result = ""
    for char in word:
        if char not in vowel:
            result += char


    print('#{} {}'.format(t, result))
