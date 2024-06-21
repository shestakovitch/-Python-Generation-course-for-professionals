"""Декоратор exception_decorator
Реализуйте декоратор exception_decorator, который возвращает

кортеж (value, 'Функция выполнилась без ошибок'), если декорируемая функция завершила свою работу без ошибок, где
value — возвращаемое значение декорируемой функции
кортеж (None, 'При вызове функции произошла ошибка'), если при выполнении декорируемой функции возникла ошибка
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также
должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор exception_decorator, но
не код, вызывающий его. """


def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except:
            return None, 'При вызове функции произошла ошибка'
    return wrapper