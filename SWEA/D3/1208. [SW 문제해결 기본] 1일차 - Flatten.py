for tc in range(10):
    n = int(input())
    boxes = list(map(int, input().split()))

    for i in range(n):
        boxes.sort()
        boxes[0] += 1
        boxes[-1] -= 1

    print('#{} {}'.format(tc+1, max(boxes)-min(boxes)))