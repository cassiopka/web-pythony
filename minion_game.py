def game_minions(s):
    vowels = set("AEIOU")
    kevin_score = 0
    stuart_score = 0
    length = len(s)

    for i in range(length):
        if s[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        return "Кевин", kevin_score
    elif kevin_score < stuart_score:
        return "Стюарт", stuart_score
    else:
        return "Ничья", kevin_score

# Пример ввода
input_string = input()
winner, score = game_minions(input_string)
print(f"{winner} {score}")

# # Test Case 1
# string = "BANANA"
# print(game_minions(string))
# # Output: ('Stuart', 12)

# # Test Case 3
# string = "AEIOU"
# print(game_minions(string))
# # Output: ('Kevin', 15)

# # Test Case 4
# string = "BCDFG"
# print(game_minions(string))
# # Output: ('Stuart', 14)

