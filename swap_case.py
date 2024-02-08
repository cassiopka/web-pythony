def swap_case(s):
    swapped = ""
    for char in s:
        if char.islower():
            swapped += char.upper()
        elif char.isupper():
            swapped += char.lower()
        else:
            swapped += char
    return swapped

s = input()
result = swap_case(s)
print(result)