"""Функция choose_plural() 🌶️🌶️
Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:

amount — натуральное число, количество
declensions — кортеж из трех вариантов склонения существительного
Функция должна возвращать строку, полученную путем объединения подходящего существительного из кортежа declensions и
количества amount, в следующем формате:

<количество> <существительное>
Примечание 1. Передаваемый в функцию кортеж легко составить по мнемоническому правилу: один, два, пять. Например:

для слова «арбуз»: арбуз, арбуза, арбузов
для слова «рубль»: рубль, рубля, рублей
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию choose_plural(), но не код,
вызывающий ее."""


def choose_plural(amount=int, declensions=tuple):
    if amount == 1 or amount % 10 == 1 and amount % 100 != 11:
        return f'{amount} {declensions[0]}'
    elif amount % 10 in (2, 3, 4) and amount % 100 not in (12, 13, 14):
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'