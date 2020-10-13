def merge_sort(div_numbers):
    if len(div_numbers) > 1:
        print(f'쪼개기: {div_numbers}')
        mid = len(div_numbers) // 2
        left_numbers = merge_sort(div_numbers[:mid])
        right_numbers = merge_sort(div_numbers[mid:])

        i, j, k = 0, 0, 0  # 왼쪽리스트 인덱스, 오른쪽 리스트 인덱스, 통합리스트인덱스
        while i < len(left_numbers) and j < len(right_numbers):
            if left_numbers[i] < right_numbers[j]:
                div_numbers[k] = left_numbers[i]
                i += 1
            else:
                div_numbers[k] = right_numbers[j]
                j += 1
            k += 1

        # 둘중 한쪽의 리스트를 다 썼음
        while i < len(left_numbers):
            div_numbers[k] = left_numbers[i]
            i += 1
            k += 1
        while j < len(right_numbers):
            div_numbers[k] = right_numbers[j]
            j += 1
            k += 1
    print(f'합치기: {div_numbers}')
    return div_numbers


numbers = [4, 2, 8, 6, 0, 5, 1, 7, 3, 9]
print(f'정렬 전: {numbers}')
print()
merge_sort(numbers)
print()
print(f'정렬 후: {numbers}')
