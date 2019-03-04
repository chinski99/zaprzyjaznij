def szlaki(a, b, c):
    n = len(a)
    d = dict()
    res = 0
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = []
        if b[i] not in d:
            d[b[i]] = []
        d[a[i]].append((b[i], c[i]))
        d[b[i]].append((a[i], c[i]))
    for k in d:
        d2 = {}
        for _, t in d[k]:
            if t not in d2:
                d2[t] = 0
            d2[t] += 1
        for t in d2:
            res += sum(range(d2[t]))
    return res


assert szlaki([1, 2, 2, 2, 5, 3], [2, 3, 4, 5, 6, 5], ['A', 'A', 'A', 'B', 'B', 'C']) == 4
assert szlaki([1, 2, 3], [2, 3, 1], ['A', 'A', 'A']) == 3
assert szlaki([2, 4, 6, 8], [4, 6, 8, 10], ['X', 'Y', 'X', 'Y']) == 0
