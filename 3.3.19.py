"""Функция is_available_date() 🌶️
Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования
номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо
период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать
номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для
бронирования. В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_available_date(), но не
код, вызывающий ее."""


from datetime import datetime


def sd(s):
    return datetime.strptime(s, '%d.%m.%Y')


def dk(spd):
    return (sd(spd[:10]), sd(spd[11:])) if '-' in spd else (sd(spd), sd(spd))


def is_available_date(sp, d):
    for x in sp:
        if not(dk(x)[1] < dk(d)[0] or dk(x)[0] > dk(d)[1]):
            return False
    return True