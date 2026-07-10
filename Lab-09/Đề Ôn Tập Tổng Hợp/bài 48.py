def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    if m > n:
        return -1

    p = 31
    mod = 10**9 + 7
    hash_pattern = 0
    hash_window = 0
    power = 1

    for i in range(m):
        hash_pattern = (hash_pattern * p + ord(pattern[i])) % mod
        hash_window = (hash_window * p + ord(text[i])) % mod
        if i < m - 1:
            power = (power * p) % mod

    for i in range(n - m + 1):
        if hash_pattern == hash_window:
            if text[i : i + m] == pattern:
                return i

        if i < n - m:
            hash_window = (
                (hash_window - ord(text[i]) * power) * p + ord(text[i + m])
            ) % mod

    return -1


print(rabin_karp("zabcd", "abc"))
