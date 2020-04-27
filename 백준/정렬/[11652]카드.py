n = int(input())

numbers_dict = {}
for _ in range(n):
    number = int(input())
    if numbers_dict.get(number):
        numbers_dict[number] += 1
    else:
        numbers_dict[number] = 1

max_cnt = max(numbers_dict.values())

result = []
for key, value in numbers_dict.items():
    if value == max_cnt:
        result.append(key)

print(min(result))
