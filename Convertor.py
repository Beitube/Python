print("Коневертор Валюты приветствует вас!")
print(
    "Доступные валюты: USD, EUR, KZT, BYN \nВНИМАНИЕ! НА ДАННЫЙ МОМЕНТ КУРС ВАЛЮТ ФИКСИРОВАННЫЙ И НЕ ОБНОВЛЯЕТСЯ"
)

kurs = {
    "USD": 90.5,  # 1 USD = 90.5 RUB
    "EUR": 98.2,  # 1 EUR = 98.2 RUB
    "KZT": 0.1533,  # 1 KZT = 0,1533 RUB
    "BYN": 26.88,  # 1 BYN = 26,88 RUB
    "RUB": 1,  # 1 RUB = 1 RUB
}

sum = float(input("Ваша сумма: "))
curV = input("Ваша валюта:").upper()
toV = input("В валюту:").upper()

if curV not in kurs:
    print("Такой валюты в базе нет!")
elif toV not in kurs:
    print("Такой валюты в базе нет!")
else:
    result = (sum * kurs[curV]) / kurs[toV]
    print(f"{sum} {curV} = {result} {toV}")
