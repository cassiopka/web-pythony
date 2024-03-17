# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_network = input('Введите IP-сеть:')
network, mask = ip_network.split('/')
binary_mask = "1" * int(mask) + "0" * (32 - int(mask))

print("Network:")
print("{:<8} {:<8} {:<8} {:<8}".format(*network.split('.')))
print("{:<8} {:<8} {:<8} {:<8}".format(*[bin(int(octet))[2:].zfill(8) for octet in network.split('.')]))
print("Mask:")
print("/{:<8}".format(mask))
print("{:<8} {:<8} {:<8} {:<8}".format(*[int(binary_mask[i:i+8], 2) for i in range(0, 32, 8)]))
print("{:<8} {:<8} {:<8} {:<8}".format(*[binary_mask[i:i+8]for i in range(0, 32, 8)]))