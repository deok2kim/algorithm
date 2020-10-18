def quick_sort(numbers):
    # 피봇을 정한다. 맨 뒤 값을 정했다.
    length = len(numbers)
    if length <= 1:
        return numbers
    else:
        pivot = numbers.pop()
        low_numbers = []
        high_numbers = []
        for i in range(length - 1):
            if numbers[i] > pivot:
                high_numbers.append(numbers[i])
            else:
                low_numbers.append(numbers[i])

        return quick_sort(low_numbers) + [pivot] + quick_sort(high_numbers)


nn = [9, 5, 1, 6, 8, 4, 2, 3, 7, 0]
print(f'정렬 전: {nn}')
print(f'정렬 후: {quick_sort(nn)}')
