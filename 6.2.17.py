"""Я и сам своего рода переводчик
Дана строка соответствия латинскому алфавиту: первый символ строки соответствует букве a, второй — b, третий — c, и так
далее. Каждый символ соответствует как заглавной, так и строчной буквам. Количество символов в строке совпадает с
количеством букв в латинском алфавите.

Напишите программу, которая с помощью данной строки переводит заданный текст.

Формат входных данных
На вход программе в первой строке подается строка соответствия латинскому алфавиту, в следующей — текст, требующий
перевода.

Формат выходных данных
Программа должна с помощью данной строки соответствия латинскому алфавиту перевести введенный текст и вывести полученный
 результат.

Примечание 1. Программа должна игнорировать все символы, не являющиеся латинскими буквами.

Примечание 2. Составить словарь соответствия можно с помощью строкового метода maketrans(), подробнее о котором
рассказывается по ссылке."""

s = input()
alfabet = {chr(i): s[i-97] for i in range(97, 97+26)}
for i in input().lower():
    if i in alfabet:
        print(alfabet[i], end='')
    else:
        print(i, end='')