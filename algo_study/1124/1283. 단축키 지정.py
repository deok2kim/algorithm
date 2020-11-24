def find_first_word(word_list):
    for i in range(len(word_list)):
        word = word_list[i]
        if word[0].upper() not in shortcut:
            return i, 0
    return False, False


def find_next_word(word_list):
    for i in range(len(word_list)):
        if word_list[i].upper() not in shortcut:
            return i
    return False


def print_first_word(word_list, list_idx, word_idx):
    a = ' '.join(word_list[:list_idx])
    b1 = word_list[list_idx][:word_idx]
    b2 = word_list[list_idx][word_idx]
    b3 = word_list[list_idx][word_idx + 1:]
    c = ' '.join(word_list[list_idx + 1:])
    shortcut.add(b2.upper())
    print(f'{a} {b1}[{b2}]{b3} {c}'.strip())


def print_next_word(word, word_idx):
    a = word[:word_idx]
    b = word[word_idx]
    c = word[word_idx + 1:]
    shortcut.add(b.upper())
    print(f'{a}[{b}]{c}')


if __name__ == '__main__':
    N = int(input())
    shortcut = set()  # 대문자 기준
    shortcut.add(' ')
    for _ in range(N):
        options = input()
        options2 = options.split()
        idx1, idx2 = find_first_word(options2)
        if idx1 is not False:
            print_first_word(options2, idx1, idx2)
        else:
            idx = find_next_word(options)
            if idx:
                print_next_word(options, idx)
            else:
                print(options)
