t = 'zero one two three four five six seven eight nine ten eleven twelve'.split()
d = dict(zip(range(10), t))
i = [d[int(n)] for n in input('Введите число: ')]
print(*i)
