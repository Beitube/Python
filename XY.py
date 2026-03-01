n = int(input())

a1 = b2 = c3 = d4 = 0

for i in range(n):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        continue
    elif x > 0 and y > 0:
        a1 += 1
    elif x > 0 and y < 0:
        b2 += 1
    elif x < 0 and y < 0:
        c3 += 1    
    elif x < 0 and y > 0:
        d4 += 1

print("Первая четверть:", a1)
print("Вторая четверть:", d4)
print("Третья четверть:", c3)
print("Четвертая четверть:", b2)
