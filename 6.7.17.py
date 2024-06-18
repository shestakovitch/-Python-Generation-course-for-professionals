"""Не поленимся и запишем
Тимур составляет список покупок, но так как на его клавиатуре перестал работать блок с цифрами, то вместо указания
количества товара числом, он добавляет его в список столько раз, сколько планирует купить. Все товары Тимур записывает в
нижнем регистре через запятую.

Напишите программу, которая выводит все товары из данного списка покупок, указывая для каждого его количество.

Формат входных данных
На вход программе подается последовательность товаров, разделенных запятой без пробелов.

Формат выходных данных
Программа должны вывести все введенные товары, указывая для каждого, сколько раз он встречается в данной
последовательности. Товары должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем
формате:

<товар>: <количество>"""

from collections import Counter

[print(f'{k}: {v}') for k, v in sorted(Counter(input().split(',')).items(), key=lambda x: x[0])]