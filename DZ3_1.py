import random

from time import time


def func_time(func):

    def wrapper(*args, **kwargs):

        function_time = time()

        result = func(*args, **kwargs)

        function_time = time() - function_time

        print(f'Время выполнения {func.__name__} составило {function_time}')
        return result

    return wrapper


#Заполняем список случайными элементами
@func_time
def rand_list(el_cnt):

    return [random.randint(1, 10) for _ in range(el_cnt)]


#Заполняем словарь случайными элементами
@func_time
def rand_dict(el_cnt):

    return {i: random.randint(1, 10) for i in range(el_cnt)}


#Удаление последнего элемента списка
@func_time
def pop_list(lst, el_cnt):

    for i in range(el_cnt):
        lst.pop()


#Удаление последнего элемента словоря
@func_time
def pop_dict(dct, el_cnt):

    for i in range(el_cnt):
        del dct[i]


#Вставка значения по индексу
@func_time
def ins_list(lst, idx):

    lst.insert(idx, random.randint(1, 10))


#Вставка значения по ключу
@func_time
def ins_dict(dct, key):

    dct[key] = random.randint(1, 10)


new_lst = rand_list(10000000)
new_dict = rand_dict(10000000)

"""
Сложность одинаковая O(n), словарь заполняется медленнее из-за расчета хешей
"""

pop_list(new_lst, 100000)
pop_dict(new_dict, 100000)

"""
Удаление с конца списка выполняется за постоянное время , т.к. не перестаивается весь список целиком.
Удаление из словоря всегда быстро , т.к один элемент не влияет на другой. Словарь не упорядочен.
"""

ins_list(new_lst, 5000)
ins_dict(new_dict, 5000)

"""
Вставка в словарь происходит мнгновенно, т.к. сложность O(n)  и при вставке в список идет перестраивание ,
Операция выполняется медленее
"""