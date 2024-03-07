def process_list_lc(arr):
    return [x * 2 if x % 2 == 0 else x ** 2 for x in arr]

def process_list_gen(arr):
    for x in arr:
        if x % 2 == 0:
            yield x * 2
        else:
            yield x ** 2
