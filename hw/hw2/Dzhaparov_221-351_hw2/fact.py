import timeit

def fact_rec(n):
    if n == 1:
        return 1
    else:
        return n * fact_rec(n - 1)

def fact_it(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    n_rec = 500
    n_it = 10000
    t1 = timeit.timeit("fact_rec({})".format(n_rec), setup="from __main__ import fact_rec", number=1)
    t2 = timeit.timeit("fact_it({})".format(n_it), setup="from __main__ import fact_it", number=1)
    print("Рекурсивная функция выполнилась за {:.6f} секунд (n = {})".format(t1, n_rec))
    print("Итерационная функция выполнилась за {:.6f} секунд (n = {})".format(t2, n_it))
