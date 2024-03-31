# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    tempInt = ""
    trunk = {}
    access = {}

    with open(config_filename, "rt") as f:
        for line in [line.strip() for line in f.readlines()]:
            if tempInt == "" and "interface" in line:
                tempInt = line.split()[-1]
            elif "trunk allowed vlan" in line:
                trunk[tempInt] = [int(item) for item in line.split()[-1].split(',')]
                tempInt = ""
            elif "access vlan" in line:
                access[tempInt] = int(line.split()[-1])
                tempInt = ""
            elif "duplex auto" in line and tempInt != "":
                access[tempInt] = 1
                tempInt = ""
    result = (access, trunk)
    return result

result = get_int_vlan_map("config_sw2.txt")
print(result)
