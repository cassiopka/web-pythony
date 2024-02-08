n = int(input("Введите целое число (n): "))

if 1 <= n <= 20:
    for i in range(n):
        print(i*i)
else:
    print("Число не соответствует диапазону от 1 до 20.")
