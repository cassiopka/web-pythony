# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ignore = ["duplex", "alias", "configuration"]

flag = False
with open(argv[1]) as f:
    result = []
    for line in f.readlines():
        for ign in ignore:
            if ign in line:
                flag = True
                break
        if flag or '!' in line:
            flag = False
            continue
        result.append(line.rstrip() + '\n')
    # result = [line.rstrip() for line in f.readlines() if '!' not in line]
    print(*result, sep="\n")
    with open(argv[2], 'w') as newfile:
        newfile.writelines(result)    

