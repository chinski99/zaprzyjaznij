from random import *


def koszulki(s):
    d = {'S': 0, 'M': 0, 'L': 0}
    for a in s:
        d[a] += 1
    return 'S' * d['S'] + 'M' * d['M'] + 'L' * d['L']


assert koszulki('MSSLS') == 'SSSML'

ls = ''.join(choices('MLS', k=200000))
print(koszulki(ls))
print(sorted(ls))
