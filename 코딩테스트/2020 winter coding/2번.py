def solution(encrypted_text, key, rotation):
    answer = ''
    n = len(encrypted_text)

    # 문자 to 숫자, 숫자 to 문자
    # a = 97, z = 122
    word_to_number = {}
    for i in range(97, 123):
        word_to_number[chr(i)] = i - 96
    number_to_word = [0]
    for i in range(97, 123):
        number_to_word.append(chr(i))

    print(word_to_number)
    print(number_to_word)

    # 먼저 돌리고
    rotation %= n
    encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation]

    # 바꾼다.
    for i in range(n):
        new_word = word_to_number[encrypted_text[i]] - word_to_number[key[i]]
        if new_word <= 0:
            new_word += 26

        print(new_word)
        answer += number_to_word[new_word]

    return answer


print(solution('qyyigoptvfb', 'abcdefghijk', 3))
print()
print(solution('rrr', 'abc', 0))
