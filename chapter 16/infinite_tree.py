def infinite_tree(a, b):
    r = 0
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
        r += 1
    return r


assert infinite_tree(4, 3) == 3
assert infinite_tree(4, 5) == 2
