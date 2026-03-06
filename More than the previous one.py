n = list(map(int, input().split()))  
count = 0
for i in range(1, len(n)):
    if n[i] > n[i - 1]:
        count += 1
print(count)
