s = '0123456789ABCDEF'


def conversion(number, deci):
    q, r = divmod(number, deci)
    n = s[r]
    if q:
        return conversion(q, deci) + n
    else:
        return n


print(conversion(10, 16))

a = int('010101', 2)
print(a)
