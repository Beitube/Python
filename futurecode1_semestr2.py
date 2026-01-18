n = int(input())
numbers = []

while n != 0:
    numbers.append(n)
    n = int(input())
result = []

for i in numbers:
    if i % len(numbers) == 0:
        result.append(i)
print(result)
