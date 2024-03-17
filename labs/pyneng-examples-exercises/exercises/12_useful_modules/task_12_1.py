# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from typing import List, Tuple
from subprocess import run, CalledProcessError, CompletedProcess
import subprocess


def ping_ip_addresses(addresses: List[str]) -> Tuple[List[str], List[str]]:
    accessible: List[str] = []
    unaccessible: List[str] = []
    for address in addresses:
        try:
            ret_value: CompletedProcess = run(['ping', '-c', '6', address], stdout=subprocess.DEVNULL)
            ret_value.check_returncode()
            accessible.append(address)
        except CalledProcessError:
            unaccessible.append(address)
    return (accessible, unaccessible)


def ping_ip_addresses2(lst):
    accessible = []
    unaccessible= []
    for i in lst:
        result = subprocess.run(['ping', '-c', '3', '-n', i])
        if result.returncode == 0:
            accessible.append(i)
        else:
            unaccessible.append(i)
    return (accessible, unaccessible)




if __name__ == "__main__":
    l = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    print(ping_ip_addresses2(l))
    pass
