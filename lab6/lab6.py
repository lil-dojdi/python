import datetime
import calendar
import re
import math

# ---------------------------
# ЗАДАНИЕ 1: Возраст в днях
# ---------------------------

def calculate_age_in_days():
    print("=== Расчет возраста в днях ===")
    
    date_pattern = r"^\d{4}-\d{2}-\d{2}$"
    
    while True:
        birth_input = input("Введите дату рождения (YYYY-MM-DD): ")
        
        if not re.match(date_pattern, birth_input):
            print("Неверный формат. Попробуйте снова.")
            continue
        
        try:
            year, month, day = map(int, birth_input.split('-'))
            birth_date = datetime.date(year, month, day)
            today = datetime.date.today()
            
            age_days = (today - birth_date).days
            print(f"Вы прожили примерно {age_days} дней.\n")
            break
        
        except ValueError:
            print("Некорректная дата. Попробуйте снова.")

# ---------------------------
# ЗАДАНИЕ 2: День недели
# ---------------------------

def find_weekday():
    print("=== Определение дня недели ===")
    
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    
    weekday_num = calendar.weekday(year, month, day)
    
    days = [
        "Понедельник", "Вторник", "Среда",
        "Четверг", "Пятница", "Суббота", "Воскресенье"
    ]
    
    print(f"Это: {days[weekday_num]}\n")

# ---------------------------
# ЗАДАНИЕ 3: Время падения
# ---------------------------

def calculate_fall_time():
    print("=== Расчет времени падения ===")
    
    while True:
        try:
            h = float(input("Введите высоту (в метрах): "))
            
            if math.isnan(h):
                print("Введите корректное число.")
                continue
            
            if h < 0:
                print("Высота не может быть отрицательной.")
                continue
            
            g = 9.8
            t = math.sqrt((2 * h) / g)
            
            print(f"Время падения: {t:.2f} секунд\n")
            break
        
        except ValueError:
            print("Ошибка ввода. Введите число.")

# ---------------------------
# ЗАДАНИЕ 4: Своя задача
# (Расчет количества дней до следующего дня рождения)
# Используем datetime + calendar
# ---------------------------

def days_until_birthday():
    print("=== Дней до следующего дня рождения ===")
    
    year = int(input("Введите год рождения: "))
    month = int(input("Введите месяц рождения: "))
    day = int(input("Введите день рождения: "))
    
    today = datetime.date.today()
    current_year = today.year
    
    next_birthday = datetime.date(current_year, month, day)
    
    if next_birthday < today:
        next_birthday = datetime.date(current_year + 1, month, day)
    
    days_left = (next_birthday - today).days
    
    weekday = calendar.day_name[next_birthday.weekday()]
    
    print(f"До следующего дня рождения осталось: {days_left} дней.")
    print(f"Он будет в день недели: {weekday}\n")

# ---------------------------
# МЕНЮ
# ---------------------------

def main():
    while True:
        print("Выберите задание:")
        print("1 - Возраст в днях")
        print("2 - День недели")
        print("3 - Время падения")
        print("4 - Дней до дня рождения")
        print("0 - Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            calculate_age_in_days()
        elif choice == "2":
            find_weekday()
        elif choice == "3":
            calculate_fall_time()
        elif choice == "4":
            days_until_birthday()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.\n")

# Запуск программы
if __name__ == "__main__":
    main()