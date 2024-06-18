"""Функция scrabble()
Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:

symbols — набор символов
word — слово
Функция должна возвращать True, если из набора символов symbols можно составить слово word, или False в противном случае.

Примечание 1. При проверке учитывается количество символов, которые нужны для составления слова, и не учитывается их
регистр.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию scrabble(), но не код,
вызывающий ее."""

from collections import Counter

def scrabble(symbols, word):
    return Counter(word.lower()) <= Counter(symbols.lower())