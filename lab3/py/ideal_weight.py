# Модуль для работы с идеальным весом

def get_valid_input(prompt, min_value, max_value, value_type=int):
    # Проверка корректности пользовательского ввода
    while True:
        try:
            value = value_type(input(prompt).strip())
            if min_value <= value <= max_value:
                return value
            print(f"Значение должно быть в диапазоне {min_value}–{max_value}.")
        except ValueError:
            print("Неверный ввод. Попробуйте снова.")

def get_valid_age():
    # Получение корректного возраста
    return get_valid_input("Возраст (в годах, >20 и <120): ", 20, 120)

def get_valid_height():
    # Получение корректного роста
    return get_valid_input("Рост (в см, от 150 до 220): ", 150, 220)

def get_valid_weight():
    # Получение корректного веса
    return get_valid_input("Текущий вес (в кг, от 45 до 300): ", 45, 300)

def get_valid_gender():
    # Получение корректного пола
    male = {"M", "m", "М", "м"}
    female = {"F", "f", "Ж", "ж", "J", "j"}
    while True:
        s = input("Пол (M/F или М/Ж): ").strip()
        if not s:
            print("Введите пол: M (мужской) или F (женский).")
            continue
        ch = s[0]
        if ch in male:
            return "M"
        if ch in female:
            return "F"
        print("Неверный ввод пола — допустимы M/F или М/Ж.")

def calculate_ideal_weight(height_cm, age_years, gender):
    # Расчет идеального веса по формуле Лоренца
    if gender == "M":
        return height_cm - 100 - ((height_cm - 150) / 4 + (age_years - 20) / 4)
    else:
        return height_cm - 100 - ((height_cm - 150) / 2.5 + (age_years - 20) / 6)

def get_recommendation(actual_weight, ideal_weight):
    # Генерация рекомендации по весу
    diff = actual_weight - ideal_weight
    if diff > 0:
        return f"Ваш вес выше положенного на {diff:.2f} кг. Рекомендуется снизить вес."
    elif diff < 0:
        return f"Вам следует набрать {-diff:.2f} кг, чтобы достичь идеала."
    return "Ваш вес равен идеальному. Отличный результат!"
