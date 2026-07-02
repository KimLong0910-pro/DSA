def first_unique(s):
    dem = {}

    for c in s:
        dem[c] = dem.get(c, 0) + 1

    for c in s:
        if dem[c] == 1:
            return c

    return None


print(first_unique("leetcode"))
