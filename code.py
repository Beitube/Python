num = input()
cnt = 0
total = 0

while int(num) % 100 != 11:
    if len(num) > 7:
        cnt += 1
    
    total += 1
    num = input()

# Обработка последнего сообщения (которое оканчивается на 11)
if len(num) > 7:
    cnt += 1
total += 1

print(f"{cnt}/{total}")
