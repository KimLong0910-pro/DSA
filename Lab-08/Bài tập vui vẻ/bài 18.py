def polynomial(s, p=31, m=10**9+7):
    hash_value = 0

    for i in s:
        hash_value = (hash_value * p + ord(i)) % m

    return hash_value

print(polynomial("abc"))