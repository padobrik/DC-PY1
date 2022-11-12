import random
import secrets
import string

def get_random_password(n = 8) -> str:
    # alphabet = string.ascii_letters + string.digits # Полезная либа для извлечения всех букв и цифр
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    alphabet = letters + digits

    return ''.join(random.sample(alphabet, n))

# Я знаю, что начиная с Python 3.6 существует модуль secrets, позволяющий генерировать такие пароли, так что мое решение:
def password_with_secrets(n = 8) -> str:
    alphabet = string.ascii_letters + string.digits

    return ''.join(secrets.choice(alphabet) for _ in range(n))


print(get_random_password())
print(password_with_secrets())