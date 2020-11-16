def countingSort(arr, digit):
    n = len(arr)

    # 배열의 크기에 맞는 output 배열을 생성하고 10개의 0을 가진 count란 배열을 생성한다.
    output = [0] * (n)
    count = [0] * (10)

    # digit, 자릿수에 맞는 count에 += 1을 한다.
    for i in range(n):
        index = arr[i] // digit
        count[index % 10] += 1
    print(count)
    # count 배열을 수정해 digit으로 잡은 포지션을 설정한다.
    for i in range(1, 10):
        count[i] += count[i - 1]
        print(i, count[i])
    print(count)

    # 결과 배열, output을 설정한다. 설정된 count 배열에 맞는 부분에 arr원소를 담는다.
    i = n - 1
    while i >= 0:
        index = arr[i] // digit
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        print(output)
    print()
    # arr를 결과물에 다시 재할당한다.
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort
def radixSort(arr):
    # arr 배열중에서 maxValue를 잡아서 어느 digit, 자릿수까지 반복하면 될지를 정한다.
    maxValue = max(arr)
    # 자릿수마다 countingSorting을 시작한다.
    digit = 1
    while int(maxValue / digit) > 0:
        countingSort(arr, digit)
        digit *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]
# arr = [4, 2, 1, 5, 7, 2]
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
