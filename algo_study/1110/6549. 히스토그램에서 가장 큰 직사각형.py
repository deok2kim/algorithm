if __name__ == '__main__':

    while True:
        tmp = input()
        if tmp == '0':
            break
        tmp = list(map(int, tmp.split()))
        n, heights = tmp[0], [0] + tmp[1:] + [0]

        check = [0]
        area = 0
        for i in range(1, n + 2):
            while check and heights[i] < heights[check[-1]]:
                cur_idx = check.pop()
                area = max(area, (i - 1 - check[-1]) * heights[cur_idx])
            check.append(i)

        print(area)
