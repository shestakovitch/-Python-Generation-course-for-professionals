"""Корректные даты
Напишите программу, которая принимает на вход последовательность дат и проверяет каждую из них на корректность.

Формат входных данных
На вход программе подается последовательность дат в формате DD.MM.YYYY, каждая на отдельной строке. Концом
последовательности является слово end.

Формат выходных данных
Программа должна для каждой введенной даты вывести текст Корректная или Некорректная в зависимости от того, является ли
дата корректной, а затем вывести количество корректных дат.

Примечание 1. Для анализа даты на корректность можете использовать уже реализованную функцию is_correct() из предыдущей
задачи."""


from datetime import date


s = 0


def is_correct(d=str):
    try:
        day, month, year = map(int, d.split('.'))
        date(year, month, day)
        global s
        s += 1
        return 'Корректная'
    except:
        return 'Некорректная'


while (d := input()) != 'end':
    print(is_correct(d))
print(s)