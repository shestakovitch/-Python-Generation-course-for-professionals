"""На Флориду с 1950 по 2017 год всего обрушилось 235 ураганов. В переменной florida_hurricane_dates хранится список
дат, в которые произошел ураган. Сезон ураганов в Атлантике официально начинается 1 июня. Дополните приведенный ниже
код, чтобы он вывел количество ураганов с 1950 года, которые обрушились на Флориду до официального начала сезона
ураганов.

Примечание 1. Считайте, что переменная florida_hurricane_dates объявлена и доступна вашей программе.

Примечание 2. Считайте, что тип date уже импортирован в программу."""


# счетчик для нужного количества ураганов
early_hurricanes = 0

# цикл по датам в которые был ураган
for hurricane in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)