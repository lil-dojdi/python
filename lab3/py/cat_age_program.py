from cat_age import validate_input, calculate_kitten_age, calculate_adult_cat_age

# Калькулятор возраста кошки
print("Калькулятор возраста кошки в человеческих годах")

is_kitten = input("Кошке меньше года? (Да/Нет): ").strip().lower()
if is_kitten in {"да", "yes"}:
    months = validate_input("Сколько месяцев кошке? (1–11): ", 1, 11)
    human_age = calculate_kitten_age(months)
    print(f"Возраст кошки в человеческих годах: {human_age}")
else:
    years = validate_input("Сколько лет кошке? (1–35): ", 1, 35)
    human_age = calculate_adult_cat_age(years)
    print(f"Возраст кошки в человеческих годах: {human_age} лет")