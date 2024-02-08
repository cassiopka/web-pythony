import re

# Чтение содержимого файла
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Нахождение слов максимальной длины
words = re.findall(r'\b\w+\b', content)  # Извлекаем все слова из текста
max_length = max(len(word) for word in words)
max_length_words = [word for word in words if len(word) == max_length]

# Вывод результата
for word in max_length_words:
    print(word)
