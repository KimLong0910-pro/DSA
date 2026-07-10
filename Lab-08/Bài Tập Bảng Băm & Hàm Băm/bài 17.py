def hash(s, m):
    tong = 0

    for i in s:
        tong += ord(i)

    return tong % m

print(hash("abc", 100))
print(hash("cba", 100))