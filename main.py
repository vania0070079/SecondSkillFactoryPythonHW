tickets = int(input("Сколько билетов вы хотите приобрести? "))
people = tickets
money = 0

while people != 0:
    age_for_ticket = int(input(f'Возраст зрителя для билета номер {people}? '))
    if age_for_ticket < 18:
        print('Для посетителя конференции возрастом менее 18 лет билет бесплатный.')

    elif 25 > age_for_ticket >= 18:
        money = money + 990
        print('Стоимость данного билета: 990 руб.')

    else:
        money = money + 1390
        print('Стоимость данного билета: 1390 руб.')
    people = people - 1

if tickets > 3:
    sale = money - (money / 10)
    print(f'Итоговая сумма к оплате {sale} руб., так как применена скидка за покупку более 3 билетов в размере 10%')

else:
    print(f'Итоговая сумма к оплате {money} руб.')