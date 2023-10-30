x = 'ABCDEF'
y = '012345'

result = []

i = 0
while i < len(x):
    result.append((x[i], y[-i]))

print(result)