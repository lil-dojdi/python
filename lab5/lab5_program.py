from employees import Employee, HourlyEmployee, SalaryEmployee
import re

def get_valid_input(prompt, pattern, error_msg):
    while True:
        value = input(prompt).strip()
        if re.match(pattern, value):
            return value
        else:
            print(error_msg)

# Создание объектов
employees = []
hourly_employees = []
salary_employees = []

print("Создание 2 объектов Employee:")
for i in range(2):
    name = get_valid_input(f"Имя сотрудника {i+1}: ", r'^[a-zA-Z]+$', "Имя должно состоять только из букв.")
    phone = get_valid_input(f"Телефон {i+1} (+373xxxxxxxx): ", r'^\+373\d{8}$', "Телефон должен соответствовать +373xxxxxxxx.")
    birth_date = get_valid_input(f"Дата рождения {i+1} (дд.мм.гггг): ", r'^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(196[0-9]|197[0-9]|198[0-9]|199[0-9]|200[0-7])$', "Дата рождения должна быть в формате дд.мм.гггг (день 01-31, месяц 01-12, год 1960-2007).")
    email = get_valid_input(f"Email {i+1}: ", r'^[a-zA-Z0-9._-]{2,20}@[a-zA-Z]{4,7}\.[a-zA-Z]{2,4}$', "Email должен содержать буквы, цифры, _-., @, домен 4-7 букв, . и 2-4 буквы.")
    specialty = get_valid_input(f"Специальность {i+1}: ", r'^[a-zA-Z]{4,20}$', "Специальность должна состоять только из букв, 4-20 символов.")
    emp = Employee(name, phone, birth_date, email, specialty)
    employees.append(emp)
    print(f"Employee {i+1} создан.")

print("\nСоздание 2 объектов HourlyEmployee:")
for i in range(2):
    name = get_valid_input(f"Имя сотрудника {i+1}: ", r'^[a-zA-Z]+$', "Имя должно состоять только из букв.")
    phone = get_valid_input(f"Телефон {i+1} (+373xxxxxxxx): ", r'^\+373\d{8}$', "Телефон должен соответствовать +373xxxxxxxx.")
    birth_date = get_valid_input(f"Дата рождения {i+1} (дд.мм.гггг): ", r'^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(196[0-9]|197[0-9]|198[0-9]|199[0-9]|200[0-7])$', "Дата рождения должна быть в формате дд.мм.гггг (день 01-31, месяц 01-12, год 1960-2007).")
    email = get_valid_input(f"Email {i+1}: ", r'^[a-zA-Z0-9._-]{2,20}@[a-zA-Z]{4,7}\.[a-zA-Z]{2,4}$', "Email должен содержать буквы, цифры, _-., @, домен 4-7 букв, . и 2-4 буквы.")
    specialty = get_valid_input(f"Специальность {i+1}: ", r'^[a-zA-Z]{4,20}$', "Специальность должна состоять только из букв, 4-20 символов.")
    while True:
        try:
            hours = float(input(f"Часы работы {i+1}: ").strip())
            if hours >= 0:
                break
            else:
                print("Часы должны быть неотрицательным числом.")
        except ValueError:
            print("Введите число.")
    while True:
        try:
            rate = float(input(f"Ставка за час {i+1}: ").strip())
            if rate > 0:
                break
            else:
                print("Ставка должна быть положительным числом.")
        except ValueError:
            print("Введите число.")
    emp = HourlyEmployee(name, phone, birth_date, email, specialty, hours, rate)
    hourly_employees.append(emp)
    print(f"HourlyEmployee {i+1} создан.")

print("\nСоздание 2 объектов SalaryEmployee:")
for i in range(2):
    name = get_valid_input(f"Имя сотрудника {i+1}: ", r'^[a-zA-Z]+$', "Имя должно состоять только из букв.")
    phone = get_valid_input(f"Телефон {i+1} (+373xxxxxxxx): ", r'^\+373\d{8}$', "Телефон должен соответствовать +373xxxxxxxx.")
    birth_date = get_valid_input(f"Дата рождения {i+1} (дд.мм.гггг): ", r'^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(196[0-9]|197[0-9]|198[0-9]|199[0-9]|200[0-7])$', "Дата рождения должна быть в формате дд.мм.гггг (день 01-31, месяц 01-12, год 1960-2007).")
    email = get_valid_input(f"Email {i+1}: ", r'^[a-zA-Z0-9._-]{2,20}@[a-zA-Z]{4,7}\.[a-zA-Z]{2,4}$', "Email должен содержать буквы, цифры, _-., @, домен 4-7 букв, . и 2-4 буквы.")
    specialty = get_valid_input(f"Специальность {i+1}: ", r'^[a-zA-Z]{4,20}$', "Специальность должна состоять только из букв, 4-20 символов.")
    while True:
        try:
            salary = float(input(f"Месячная зарплата {i+1}: ").strip())
            if salary > 0:
                break
            else:
                print("Зарплата должна быть положительным числом.")
        except ValueError:
            print("Введите число.")
    emp = SalaryEmployee(name, phone, birth_date, email, specialty, salary)
    salary_employees.append(emp)
    print(f"SalaryEmployee {i+1} создан.")

# Вывод значений свойств
print("\nСвойства Employee:")
for i, emp in enumerate(employees):
    print(f"Employee {i+1}: Имя={emp.name}, Телефон={emp.phone}, Дата={emp.birth_date}, Email={emp.email}, Специальность={emp.specialty}")

print("\nСвойства HourlyEmployee:")
for i, emp in enumerate(hourly_employees):
    print(f"HourlyEmployee {i+1}: Имя={emp.name}, Телефон={emp.phone}, Дата={emp.birth_date}, Email={emp.email}, Специальность={emp.specialty}, Часы={emp.hours_worked}, Ставка={emp.hourly_rate}")

print("\nСвойства SalaryEmployee:")
for i, emp in enumerate(salary_employees):
    print(f"SalaryEmployee {i+1}: Имя={emp.name}, Телефон={emp.phone}, Дата={emp.birth_date}, Email={emp.email}, Специальность={emp.specialty}, Зарплата={emp.monthly_salary}")

# Вывод зарплат
hourly_salaries = [emp._calculateSalary() for emp in hourly_employees]
salary_salaries = [emp._calculateSalary() for emp in salary_employees]

print(f"\nЗарплаты HourlyEmployee: {hourly_salaries}")
print(f"Зарплаты SalaryEmployee: {salary_salaries}")