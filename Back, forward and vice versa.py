n = input().split()
for i in range(0, len(n) - 1, 2):
    n[i], n[i + 1] = n [i + 1], n[i]
print(' '.join(n))

