def quick_sort(numbers, start, end):
    if start >= end:  # 원소가 1개인 경우
        return

    pivot = start  # pivot 가장 왼쪽의 원소
    i = start + 1
    j = end
    while i <= j:  # 엇갈릴 때 까지 반복
        while i <= j:
            if numbers[i] >= numbers[pivot]:  # pivot 보다 큰 값을 만날 때
                break
            else:
                i += 1
        while j >= i:
            if numbers[j] <= numbers[pivot]:  # pivot 보다 작은 값을 만날 때
                break
            else:
                j -= 1

        if j < i:  # 엇갈리면 pivot 과 작은값을 교체
            numbers[pivot], numbers[j] = numbers[j], numbers[pivot]
        else:  # 엇갈리지 않았다면 큰값(i)와 작은값(j)를 교체
            numbers[i], numbers[j] = numbers[j], numbers[i]
        print(f'정렬 중: {numbers}')

    # 교체한 작은값(j)는 fix!! fix 된 값을 기준으로 양쪽으로 나눠서 분할정복
    quick_sort(numbers, start, j - 1)
    quick_sort(numbers, j + 1, end)


numbers = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
print(f'정렬 전: {numbers}')
print()

quick_sort(numbers, 0, len(numbers) - 1)

print()
print(f'정렬 후: {numbers}')

nn = [9, 5, 1, 6, 8, 4, 2, 3, 7, 0]
quick_sort(nn, 0, 9)
