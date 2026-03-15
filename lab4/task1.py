import re

# Паттерны для проверки номеров телефонов Молдовы
patterns = [
    r'^00373\d{8}$',  # 00373 + 8 цифр
    r'^\+373\d{8}$',  # +373 + 8 цифр
    r'^\d{8}$',       # 8 цифр
    r'^0\d{8}$'       # 0 + 8 цифр
]

while True:
    try:
        phone = input("Введите номер телефона: ")
        for pattern in patterns:
            if re.match(pattern, phone):
                print(f"Номер {phone} корректен. Отлично!")
                break
        else:
            raise ValueError("Неверный формат номера телефона.")
        break  
    except ValueError as e:
        print(e)
        continue