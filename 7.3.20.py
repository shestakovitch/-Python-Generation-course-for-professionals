"""Январь, февраль, ...
Напишите программу с использованием конструкции try-except, которая выводит название месяца, соответствующее введенному
целому числу (от 1 до 12 включительно), причем если введенное число не принадлежит отрезку [1;12], программа должна
вывести текст:
Введено число из недопустимого диапазона
если введенное значение не является целым числом, программа должна вывести текст:
Введено некорректное значение
Формат входных данных
На вход программе подается единственная строка с произвольным значением.

Формат выходных данных
Программа должна вывести полное название месяца на английском, соответствующее введенному числу (от 1 до 12
включительно) или текст с соответствующей ошибкой, если введенное значение некорректно.

Примечание 1. Для получения списка с названиями месяцев вспомните атрибут month_name из модуля calendar."""

months = {1: 'January',
          2: 'February',
          3: 'March',
          4: 'April',
          5: 'May',
          6: 'June',
          7: 'July',
          8: 'August',
          9: 'September',
          10: 'October',
          11: 'November',
          12: 'December'}
try:
    print(months[int(input())])
except KeyError:
    print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')