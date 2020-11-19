if __name__ == '__main__':
    N = int(input())
    max_five = N // 5
    for i in range(max_five, -1, -1):
        five = i
        three = (N - 5 * i) // 3
        if five * 5 + three * 3 == N:
            print(five + three)
            break
    else:
        print(-1)
