n = int(input())
len_n = len(list(str(n)))

expect_result = n - (len_n-1)*9
result = 0

while True:
    str_number = str(expect_result)
    list_number = list(map(int, str_number))
    result = expect_result + sum(list_number)

    if result == n:
        break
    else:
        expect_result += 1

    if expect_result >= n:
        expect_result = 0
        break

print(expect_result)
