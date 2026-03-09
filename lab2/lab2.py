#задание 2. сортировка по второму элементу в кортеже
"""
data = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 2), (10, 45)]

result = sorted(data, key=lambda item: item[1])

print(result)
"""
#задание 3. сортировка четных чисел
"""
numbers = [1, 5, 8, 10, 13, 16, 20]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
"""
#задание 4. 
"""
# 1. Без параметров
def show_welcome():
    print("--- Добро пожаловать в систему Python-задач ---")

# 2. С параметрами и возвращающая результат
def calculate_total(price, quantity):
    return price * quantity

# 3. С предопределенным значением и return
def apply_discount(amount, discount=0):
    final_price = amount - (amount * discount / 100)
    return final_price
"""
#задание 5.
def average_mark(test, laboratory, exam, individual):
    
    if not (5 <= test <= 10): return "Неверная оценка!"
    elif not (5 <= laboratory <= 10): return "Неверная оценка!"
    elif not (5 <= exam <= 10): return "Неверная оценка!"
    elif not (5 <= individual <= 10): return "Неверная оценка!"
    else:
        avg = (test + laboratory + exam + individual) / 4
        return "Зачёт" if avg >= 5 else "Не зачёт"


try:
    print("Введите ваши оценки (от 1 до 10):")
    t = int(input("Тест: "))
    l = int(input("Лабораторная: "))
    e = int(input("Экзамен: "))
    i = int(input("Индивидуальное: "))

    final_result = average_mark(t, l, e, i)
    print(f"\nИтог: {final_result}")

except ValueError:
    print("Ошибка! Нужно вводить только целые числа.")
