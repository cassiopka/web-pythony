import sys

def my_sum(*args):
    return sum(args)

if __name__ == "__main__":
    args = [float(x) for x in sys.argv[1:]]
    result = my_sum(*args)
    print(result)
