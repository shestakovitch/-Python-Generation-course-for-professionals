"""Функция triangle() 😥
Реализуйте функцию triangle() с использованием рекурсии, которая принимает один аргумент:

h — натуральное число
Функция должна выводить звездный треугольник с высотой h в соответствии со следующим примером:

...
*****
****
***
**
*
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию triangle(), но не код,
вызывающий ее."""


def triangle(h: int):
    if h > 0:
        print('*' * h)
        triangle(h - 1)
