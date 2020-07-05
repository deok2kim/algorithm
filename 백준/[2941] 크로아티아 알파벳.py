word = input()
croatia = {
    'c=': 'a',
    'c-': 'b',
    'dz=': 'c',
    'd-': 'd',
    'lj': 'e',
    'nj': 'f',
    's=': 'g',
    'z=': 'h',
}

start = 0
cnt = 0
while True:
    if croatia.get(word[start:start+2]):
        start += 2
        cnt += 1

    elif croatia.get(word[start:start+3]):
        start += 3
        cnt += 1

    else:
        start += 1

    if start == len(word) - 1:
        break

print(cnt)