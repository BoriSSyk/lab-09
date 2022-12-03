T = set(i for i in range(101, 251) if i % 3 == 0)
print(*T)
T -= set(i for i in range(101, 251) if i % 6 == 0)
print(*T)
