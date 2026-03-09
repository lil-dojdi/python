from ideal_weight import get_valid_input, calculate_ideal_weight, get_recommendation

# Калькулятор идеального веса
print("Калькулятор идеального веса (формула Лоренца)")

age = get_valid_input("Возраст (20–120 лет): ", 20, 120)
height = get_valid_input("Рост (150–220 см): ", 150, 220, float)
gender = get_valid_input("Пол (1 - Мужской, 2 - Женский): ", 1, 2)
actual_weight = get_valid_input("Текущий вес (45–300 кг): ", 45, 300, float)

gender = "M" if gender == 1 else "F"
ideal_weight = calculate_ideal_weight(height, age, gender)
recommendation = get_recommendation(actual_weight, ideal_weight)

print(f"\nВаш идеальный вес: {ideal_weight:.2f} кг")
print(recommendation)