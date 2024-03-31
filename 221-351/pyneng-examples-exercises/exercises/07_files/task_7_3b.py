# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
n = input('номер влан: ')
with open("CAM_table.txt", "r") as file:
    a = []
    for line in file:

            if "DYNAMIC" in line:
                line_list = line.split()
                if line_list[0].isdigit() and line_list[0] ==n:
                    vlan = line_list[0]
                    mac_address = line_list[1]
                    interface = line_list[3]
                    a.append([int(vlan), mac_address, interface])

for elem in sorted(a):
     print("{:<8}{:<20}{:<8}".format(*elem))
    
                    