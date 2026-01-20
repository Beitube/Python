n = int(input())

for h in range(24):
    m = h**n
    if 0 <= m <= 59:
        print(f"{h:02d}:{m:02d}")
