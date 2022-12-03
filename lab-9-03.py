keys = ('O', 'H', 'N', 'P')
d = {k: input(f'{k}: ') for k in keys}

print(sorted(d.items(), key=lambda x: x[1]))
