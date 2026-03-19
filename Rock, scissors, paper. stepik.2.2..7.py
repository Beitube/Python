timur = input()
ruslan = input()

if timur in ['камень'] and ruslan in ['бумага']:
    print('Руслан')
elif timur == ruslan:
    print('ничья')
elif timur in ['ножницы'] and ruslan in ['камень']:   
    print('Руслан')
elif timur in ['бумага'] and ruslan in ['ножницы']:    
    print('Руслан')
else:
    print('Тимур')
