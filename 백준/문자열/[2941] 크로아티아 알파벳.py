word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

idx = 0
cnt = 0
while True:
    if word[idx:idx+2] in croatia:
        idx += 2
        cnt += 1

    elif word[idx:idx+3] in croatia:
        idx += 3
        cnt += 1

    else:
        idx += 1
        cnt += 1

    if idx == len(word):
        break

print(cnt)