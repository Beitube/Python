a = input().split()
n = []
for i in range(len(a)):
    if a[i] not in n:
        n.append(a[i])
print(len(n))  
