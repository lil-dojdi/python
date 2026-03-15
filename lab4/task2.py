import re
import os

DATA_FILE = 'data.txt'

def validate_name(name):
    # Только буквы, 2-20 символов, возможно несколько -
    if not (2 <= len(name) <= 20):
        return False
    if not re.match(r'^[a-zA-Z]+(-[a-zA-Z]+)*$', name):
        return False
    return True

def validate_department(dept):
    # Буквы, цифры, один пробел максимум
    if '  ' in dept:  # более одного пробела
        return False
    if not re.match(r'^[a-zA-Z0-9]+( [a-zA-Z0-9]+)?$', dept):
        return False
    return True

def input_data():
    while True:
        surname = input("Введите фамилию сотрудника: ").strip()
        name = input("Введите имя сотрудника: ").strip()
        department = input("Введите отдел: ").strip()
        try:
            children = int(input("Введите количество детей (0-19): ").strip())
        except ValueError:
            print("Количество детей должно быть целым числом.")
            continue

        if not validate_name(surname):
            print("Фамилия должна содержать только буквы, 2-20 символов, возможно один '-'.")
            continue
        if not validate_name(name):
            print("Имя должно содержать только буквы, 2-20 символов, возможно один '-'.")
            continue
        if not validate_department(department):
            print("Отдел должен содержать буквы и цифры, не более одного пробела.")
            continue
        if not (0 <= children <= 19):
            print("Количество детей должно быть от 0 до 19.")
            continue

        # Заменить пробелы в отделе на _
        department = department.replace(' ', '_')

        # Сохранить в файл
        with open(DATA_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{surname}\t{name}\t{department}\t{children}\n")
        print("Данные сохранены.")
        break

def view_data():
    if not os.path.exists(DATA_FILE):
        print("Файл данных не найден.")
        return
    total_children = 0
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print("Список сотрудников:")
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) == 4:
            surname, name, dept, children_str = parts
            try:
                children = int(children_str)
                total_children += children
                dept = dept.replace('_', ' ')  # Вернуть пробелы для вывода
                print(f"{surname} {name}, отдел: {dept}, детей: {children}")
            except ValueError:
                continue
    print(f"Общее количество детей: {total_children}")

def view_childless():
    if not os.path.exists(DATA_FILE):
        print("Файл данных не найден.")
        return
    childless = []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) == 4:
            surname, name, dept, children_str = parts
            try:
                children = int(children_str)
                if children == 0:
                    childless.append(f"{surname} {name}")
            except ValueError:
                continue
    if childless:
        print("Бездетные сотрудники:")
        for emp in childless:
            print(emp)
    else:
        print("Все сотрудники имеют детей.")

def main():
    while True:
        print("\nМеню:")
        print("1. Ввод данных")
        print("2. Просмотр данных о детях")
        print("3. Список бездетных сотрудников")
        print("4. Выход")
        choice = input("Выберите опцию: ").strip()
        if choice == '1':
            input_data()
        elif choice == '2':
            view_data()
        elif choice == '3':
            view_childless()
        elif choice == '4':
            break
        else:
            print("Неверный выбор.")


