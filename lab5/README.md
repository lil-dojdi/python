# Лабораторная работа №5: Программирование в Python

## Классы и объекты в Python. Соблюдение принципов инкапсуляции и наследования

---

### Задание a: Определите класс «Employee»

**Описание:**  
Определить базовый класс Employee с приватными переменными (__name, __phone, __birth_date, __email, __specialty), публичным методом calculateAge() (pass) и защищенным методом calculateSalary() (pass).

**Пример кода:**
```python
class Employee:
    def __init__(self, name, phone, birth_date, email, specialty):
        self.__name = name
        self.__phone = phone
        self.__birth_date = birth_date
        self.__email = email
        self.__specialty = specialty

    def calculateAge(self):
        # Публичный метод
        pass

    def _calculateSalary(self):
        # Защищенный метод
        pass
```

**Объяснение:**  
Класс Employee инициализирует приватные атрибуты через __init__. calculateAge() публичный (без подчеркиваний), calculateSalary() защищенный (одно подчеркивание).

---

### Задание b: Создайте setter-ы и getter-ы

**Описание:**  
Создать getter-ы и setter-ы для всех свойств с property() и декораторами. Объяснить разницу.

**Пример кода:**
```python
@property
def name(self):
    return self.__name

@name.setter
def name(self, value):
    if re.match(r'^[a-zA-Z]+$', value):
        self.__name = value
    else:
        raise ValueError("Имя должно состоять только из букв.")
```

**Объяснение:**  
property() создает дескриптор для доступа к приватным атрибутам. Декораторы @property для getter, @name.setter для setter. Разница: property() позволяет управлять доступом, валидацию; без них атрибуты публичны.

---

### Задание c: Определите производные классы

**Описание:**  
Создать HourlyEmployee и SalaryEmployee, наследующие от Employee, с дополнительными приватными свойствами и инкапсуляцией.

**Пример кода:**
```python
class HourlyEmployee(Employee):
    def __init__(self, name, phone, birth_date, email, specialty, hours_worked, hourly_rate):
        super().__init__(name, phone, birth_date, email, specialty)
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__hours_worked = value
        else:
            raise ValueError("Часы должны быть неотрицательным числом.")
```

**Объяснение:**  
Наследование через super().__init__(). Дополнительные свойства приватные, с getter/setter для инкапсуляции.

---

### Задание d: Переопределите calculateSalary

**Описание:**  
В HourlyEmployee: зарплата = часы * ставка. В SalaryEmployee: зарплата = месячная.

**Пример кода:**
```python
def _calculateSalary(self):
    return self.__hours_worked * self.__hourly_rate
```

**Объяснение:**  
Переопределение метода в дочерних классах для специфической логики расчета.

---

### Задание e: Создайте 6 объектов

**Описание:**  
Создать по 2 объекта каждого типа с input() и валидацией через regex.

**Пример кода:**
```python
name = get_valid_input("Имя: ", lambda x: re.match(r'^[a-zA-Z]+$', x) or ValueError("..."))
emp = Employee(name, phone, birth_date, email, specialty)
```

**Объяснение:**  
Функция get_valid_input запрашивает ввод, проверяет regex, повторяет при ошибке. Setter-ы вызываются при создании.

---

### Задание f: Вызовите getter-ы

**Описание:**  
Вывести все свойства через getter-ы для 6 объектов.

**Кусок кода:**
```python
print(f"Имя={emp.name}, Телефон={emp.phone}...")
```

**Объяснение:**  
Getter-ы возвращают значения приватных атрибутов.

---

### Задание g: Выведите зарплаты

**Описание:**  
Вывести зарплаты в виде списков по типу найма.

**Кусок кода:**
```python
hourly_salaries = [emp._calculateSalary() for emp in hourly_employees]
print(f"Зарплаты HourlyEmployee: {hourly_salaries}")
```

**Объяснение:**  
Списки comprehension, вызов защищенного метода для расчета.