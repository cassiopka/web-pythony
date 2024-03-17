import re

def wrapper(f):
    def fun(l):
        normalized_and_formatted_phones = []
        for phone in l:
            phone_number = re.sub(r'\D', '', phone)
            if len(phone_number) == 11 and phone_number.startswith('8'):
                phone_number = '7' + phone_number[1:]
            elif len(phone_number) == 10:
                phone_number = '7' + phone_number
            normalized_and_formatted_phones.append('+7 ({}) {}-{}-{}'.format(phone_number[1:4], phone_number[4:7], phone_number[7:9], phone_number[9:]))
        return f(normalized_and_formatted_phones)
    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')
