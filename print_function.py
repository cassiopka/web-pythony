n = int(input("Введите целое число (n): "))

if 1 <= n <= 20:
    for i in range(1, n+1):
        print(i, end="")
else:
    print("Число не соответствует диапазону от 1 до 20.")
    