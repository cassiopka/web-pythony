s = input()
swapped = ""
for char in s:
    if char.islower():
        swapped += char.upper()
    elif char.isupper():
        swapped += char.lower()
    else:
        swapped += char

print(swapped)
