
def validate_input(prompt, min_value, max_value, value_type=int):
    # Проверка корректности пользовательского ввода
    while True:
        try:
            value = value_type(input(prompt).strip())
            if min_value <= value <= max_value:
                return value
            print(f"Значение должно быть в диапазоне {min_value}–{max_value}.")
        except ValueError:
            print("Неверный ввод. Попробуйте снова.")


def calculate_kitten_age(months):
    # Расчет возраста котенка в человеческих годах
    kitten_age_map = {
        1: "6 месяцев",
        2: "10 месяцев",
        3: "2 года",
        4: "5 лет",
        5: "8 лет",
        6: "14 лет",
        7: "15 лет",
        8: "16 лет",
        9: "16 лет",
        10: "17 лет",
        11: "17 лет",
    }
    return kitten_age_map.get(months, "Возраст не найден.")


def calculate_adult_cat_age(years):
    # Расчет возраста взрослой кошки в человеческих годах
    if years == 1:
        return 18
    elif years == 2:
        return 25
    elif 3 <= years <= 15:
        return 25 + (years - 2) * 4
    else:
        return 25 + (15 - 2) * 4 + (years - 15) * 3