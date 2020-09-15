def check_pal(w):
    left = w[:len(w) // 2]
    w.reverse()
    right = w[:len(w) // 2]
    # print(left)
    # print(right)
    if left == right:
        return True


if __name__ == "__main__":
    word = input()
    word = list(word)
    for i in range(len(word)):
        if check_pal(word[i:]):
            add_word = word[:i]
            add_word.reverse()
            word += add_word
            break

    # print(word)
    print(len(word))
