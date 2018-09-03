def travel(cities_no, cash, highways):
    results = [[0] * cities_no for i in range(cash + 1)]
    for i in range(cities_no):
        results[0][i] = i

    for i in range(1, cash + 1):
        for j in range(cities_no):
            results[i][j] = results[i - 1][j]
        for j in range(cities_no):
            if highways[j] > -1:
                k = highways[j]
                results[i][k] = min(results[i][k], results[i - 1][j] + 1)
        for j in range(1,cities_no):
            results[i][j]=min(results[i][j],results[i][j-1]+1)
    print(results)
    return results[-1][-1]


assert travel(6, 0, [2, -1, 5, 1, 1, -1]) == 5
assert travel(6, 1, [2, -1, 5, 1, 1, -1]) == 3
assert travel(6, 2, [2, -1, 5, 1, 1, -1]) == 2
assert travel(4, 1, [2, -1, -1, -1]) == 2
