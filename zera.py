from random import *

t1 = [[10, 100, 10], [1, 10, 1], [1, 10, 1]]
t2 = [[12, 25, 1, 15], [6, 25, 4, 10], [7, 15, 15, 5]]


def ilezer(n):
    a = b = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    while n % 5 == 0:
        n //= 5
        b += 1
    return (a, b)


assert ilezer(4 * 125) == (2, 3)


def convert(tbl):
    x = tbl.copy()
    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] = ilezer(x[i][j])
    return x


assert convert([[1, 2], [4, 25]]) == [[(0, 0), (1, 0)], [(2, 0), (0, 2)]]


def my_sum(a, b):
    if isinstance(a, int):
        return a + b
    else:
        return tuple(sum(x) for x in zip(a, b))


assert my_sum(1, 5) == 6
assert my_sum((1, 2), (3, 4)) == (4, 6)


def my_diff(a, b):
    if isinstance(a, int):
        return a - b
    else:
        return tuple(x[0] - x[1] for x in zip(a, b))


assert my_diff(1, 5) == -4
assert my_diff((1, 2), (3, 4)) == (-2, -2)


def build_prefix_sums(tbl):
    n = len(tbl)
    res = []
    for i in range(n):
        m = len(tbl[0])
        w = [tbl[i][0]]
        for j in range(1, m):
            w.append(my_sum(w[-1], tbl[i][j]))
        res.append(w)
    return res


def rotate(t):
    return [list(a) for a in zip(*t)]


def invert(t):
    return [a[::-1] for a in t]


assert invert(rotate([[1, 2, 3], [4, 5, 6]])) == [[4, 1], [5, 2], [6, 3]]


def max_in_tbl(tbl):
    rows = len(tbl)
    cols = len(tbl[0])
    rot_tbl = rotate(tbl)
    pref_hor = build_prefix_sums(tbl)
    pref_ver = build_prefix_sums(rot_tbl)
    res = 0
    for i in range(rows):
        for j in range(cols):
            r = pref_hor[i][j]
            if i > 0:
                r = max(r, r + pref_ver[j][i - 1])
            if i < rows - 1:
                r = max(r, r + pref_ver[j][rows - 1] - pref_ver[j][i])
            res = max(res, r)
    return res


test_t_2 = [[1, 5, 7, 3], [4, 2, 1, 8], [6, 5, 4, 0]]
assert max_in_tbl(test_t_2) == 26

test_t = [[1, 3, 5], [2, 1, 4]]
assert build_prefix_sums(test_t) == [[1, 4, 9], [2, 3, 7]]
assert build_prefix_sums([list(a) for a in zip(*test_t)]) == [[1, 3], [3, 4], [5, 9]]
assert build_prefix_sums([list(a) for a in zip(*test_t)])[1][1] == 4


def max_in_tbl_tpl(tbl):
    rows = len(tbl)
    cols = len(tbl[0])
    rot_tbl = rotate(tbl)
    pref_hor = build_prefix_sums(tbl)
    pref_ver = build_prefix_sums(rot_tbl)
    res = (0, 0)
    for i in range(rows):
        for j in range(cols):
            r = pref_hor[i][j]
            ru = rd = (0, 0)
            if i > 0:
                ru = my_sum(r, pref_ver[j][i - 1])
            if i < rows - 1:
                down = my_diff(pref_ver[j][rows - 1], pref_ver[j][i])
                rd = my_sum(r, down)
            res = max(res, r, ru, rd, key=min)
    return res


ttp = convert(invert(rotate(t1)))
print(ttp)
assert max_in_tbl_tpl(ttp) == (5, 5)


def check_rotations(tbl):
    w = 0
    for i in [tbl, invert(tbl), rotate(tbl), invert(rotate(tbl))]:
        p = max_in_tbl_tpl(i)
        print(p)
        w = max(w, min(p))
    return w


# assert check_rotations(test_t) == 13


def zera(tbl):
    n_tbl = convert(tbl)
    return check_rotations(n_tbl)

assert zera(t1) == 5
assert zera(t2) == 4


def big_test():
    big_tbl = [[randint(1,10**9)]*200 for _ in range(200)]
    print(zera(big_tbl))


big_test()
