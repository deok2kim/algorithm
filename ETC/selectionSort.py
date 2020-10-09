numbers = [5, 3, 8, 1, 2]
print(f'정렬 전: {numbers}')
print()
for i in range(len(numbers)):
    print(f'{i + 1}세트')
    min_number = 99
    idx = 0
    for j in range(i, len(numbers)):
        if numbers[j] < min_number:
            min_number = numbers[j]
            idx = j
    else:
        numbers[i], numbers[idx] = numbers[idx], numbers[i]
    print(f'정렬 중: {numbers}')
print()
print(f'정렬 후: {numbers}')
