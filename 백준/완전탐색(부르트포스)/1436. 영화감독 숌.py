if __name__ == '__main__':
    N = int(input())
    i = 1666
    answer = 666
    cnt = 1
    while cnt < N:

        six_cnt = 0
        for num in str(i):
            if num == '6':
                six_cnt += 1
            else:
                six_cnt = 0
            if six_cnt == 3:
                answer = i
                cnt += 1
                break

        i += 1

    print(answer)
