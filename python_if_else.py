n = int(input("Введите целое число: "))

if 1 <= n <= 100:
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
else:
    print("Число не соответствует диапазону от 1 до 100.")
