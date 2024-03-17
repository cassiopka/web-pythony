# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate

from task_12_1 import ping_ip_addresses, ping_ip_addresses2



def print_ip_table(accessible, unaccessible):
    # columns = ['Reachable', 'Unreachable']
    list_of_dict = {
        'Reachable': accessible,
        'Unreachable': unaccessible
    }
    print(tabulate(list_of_dict, headers='keys'))



Reachable = ["10.10.1.7", "10.10.1.8", "10.10.1.9", "10.10.1.15"]
Unreachable = ["10.10.2.1", "10.10.1.2"]

print_ip_table(Reachable, Unreachable)