n = input()

r_n = n[::-1]

g = []
for i in range(0, len(r_n), 3):
    g.append(r_n[i:i+3])

result = ','.join(g)[::-1]

print(result)
