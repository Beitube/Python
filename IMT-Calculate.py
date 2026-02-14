m = float(input())
h = float(input())

IMT = m / (h * h)

if 18.5 <= IMT <= 25:
    print("Оптимальная масса")
elif IMT < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")
