# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

flag = False
with open('config_sw1.txt') as f:
    result = []
    for line in f.readlines():
        for ign in ignore:
            if ign in line:
                flag = True
                break
        if flag or '!' in line:
            flag = False
            continue
        result.append(line.rstrip())
    # result = [line.rstrip() for line in f.readlines() if '!' not in line]
    print(*result, sep="\n")        

