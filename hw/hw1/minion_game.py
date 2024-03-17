vowels = set("AEIOU")
kevin_score = 0
stuart_score = 0

input_string = input()
length = len(input_string)

for i in range(length):
    if input_string[i] in vowels:
        kevin_score += length - i
    else:
        stuart_score += length - i

if kevin_score > stuart_score:
    print("Кевин", kevin_score)
elif kevin_score < stuart_score:
    print("Стюарт", stuart_score)
else:
    print("Ничья", kevin_score)
