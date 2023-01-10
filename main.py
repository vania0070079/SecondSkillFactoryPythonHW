money = int(input("Здравствуйте! Введите сумму пополнения: "))
per_cent = {'ТКБ': 5.6,
            'СКБ': 5.9,
            'ВТБ': 4.28,
            'СБЕР': 4.0}
deposit = []
for i in per_cent:
    deposit.append(per_cent[i] * money / 100)
max_deposit = max(deposit)
print(deposit)
print ("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))