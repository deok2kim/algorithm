numbers = [5, 3, 8, 1, 2]
print(f'정렬 전: {numbers}')
print()
for i in range(len(numbers)):
    print(f'{i + 1}세트')
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            print(f'정렬 중: {numbers}')
print()
print(f'정렬 후: {numbers}')
