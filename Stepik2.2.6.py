n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
y = int(input())
p = "НЕТ"
for j in range(0, len(a)):
    for k in range(0, len(a)):
        if j != k:
            if a[j] * a[k] == y:
                p = "ДА"
print(p)              
