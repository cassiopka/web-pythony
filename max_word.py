import re

with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()

words = re.findall(r'\b\w+\b', content)  
max_length_words = [word for word in words if len(word) == max_length]

# Вывод результата
for word in max_length_words:
    print(word)
