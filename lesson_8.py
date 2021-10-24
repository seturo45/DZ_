# задание 1

import re
EMAIL = re.compile(r'([A-Za-z0-9.]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    email_check = EMAIL.findall(email)[0]
    if email_check:
        name, address = email_check
        print(f'Задание_1)', {'username': name, 'domain': address})
    else:
        raise ValueError(f'wrong email: {email}')


email_parse('nikita.kutyaev@gmail.com')


# задание 3
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        """Действие декоратора в задании 3 НЕ скрыто"""
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)
    return wrapper


@type_logger
def calc_cube(*args):
    """В задании 3 действие декоратора скрыто"""
    return list(map(lambda x: x ** 3, args))


a = calc_cube(int(input('Задание_3) Введите число: ')))
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)


# задание 4
def val_checker(decorator_check_func):
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)
        def wrapped(x):
            """Декоратор в задании 4 НЕ скрыт"""
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(f"Incorrect number: {x}")

        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Декоратор в задании 4 скрыт"""
    return x ** 3

a = calc_cube(int(input('Task_4) Enter your number: ')))
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)