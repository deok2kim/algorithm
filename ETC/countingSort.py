N = 5  # 5 이하인 수들을 정렬해라
numbers = [1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 3,
           3, 2, 1, 2, 3, 1, 2, 3, 4, 1, 5, 1,
           2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3,
           4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(f'정렬 전: {numbers}')
count_list = [0] * (N + 1)

for number in numbers:
    count_list[number] += 1

sorted_numbers = []
for i in range(len(count_list)):
    for j in range(count_list[i]):
        sorted_numbers.append(i)

print(f'정렬 후: {sorted_numbers}')
