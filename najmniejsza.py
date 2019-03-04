def najmniejsza(n):
    x = n // 9
    y = n % 9
    if y:
        return int(str(y) + '9' * x)
    else:
        return int('9' * x)


assert najmniejsza(20) == 299
assert najmniejsza(18) == 99
assert najmniejsza(5) == 5
assert najmniejsza(36) == 9999
