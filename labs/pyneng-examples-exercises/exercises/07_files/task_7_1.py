# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

template = [
    "Prefix",
    "AD/Metric",
    "Next-Hop",
    "Last update",
    "Outbound Interface"
]

with open("ospf.txt", 'rt') as f:
    for line in f.readlines():
        result = []
        for param in line.replace(',', '').replace("via", '').replace('O', '').strip().split():
            result.append(param.strip('[]'))
        for pair in zip(template, result):
            print(f"{pair[0]:22}{pair[1]}")

        print("\n")
