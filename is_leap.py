def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Считываем год из стандартного потока ввода
year = int(input())

# Проверяем, является ли год високосным и выводим результат
print(is_leap_year(year))