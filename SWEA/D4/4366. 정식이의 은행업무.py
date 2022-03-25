def convert_decimal(standard, num):
    converted_number = 0
    for i in range(len(num)):
        converted_number += int(num[i]) * (standard ** (len(num) - i - 1))
    return converted_number


T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    binary_number = input()
    trinary_number = input()

    guess_number_list = {}

    for i in range(len(binary_number)):
        for j in range(2):
            if binary_number[i] == str(j):
                continue

            wrong_number = str(j)
            changed_number = binary_number[:i] + wrong_number + binary_number[i + 1:]
            guess_number = convert_decimal(2, changed_number)
            guess_number_list[guess_number] = 1

    for i in range(len(trinary_number)):
        for j in range(3):
            if trinary_number[i] == str(j):
                continue

            wrong_number = str(j)
            changed_number = trinary_number[:i] + wrong_number + trinary_number[i + 1:]
            guess_number = convert_decimal(3, changed_number)
            if guess_number_list.get(guess_number):
                answer = guess_number
                break

    print(f'#{test_case} {answer}')
