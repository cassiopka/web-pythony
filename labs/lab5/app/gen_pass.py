import bcrypt

password = "password123".encode()  # Преобразуйте пароль в байты
salt = bcrypt.gensalt()           # Сгенерируйте соль
hashed = bcrypt.hashpw(password, salt)  # Сгенерируйте хеш

print(hashed.decode())            # Выведите хеш в виде строки