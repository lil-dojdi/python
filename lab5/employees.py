import re

class Employee:
    def __init__(self, name, phone, birth_date, email, specialty):
        self.name = name  # Вызывает setter
        self.phone = phone
        self.birth_date = birth_date
        self.email = email
        self.specialty = specialty

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if re.match(r'^[a-zA-Z]+$', value):
            self.__name = value
        else:
            raise ValueError("Имя должно состоять только из букв.")

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if re.match(r'^\+373\d{8}$', value):
            self.__phone = value
        else:
            raise ValueError("Телефон должен соответствовать +373xxxxxxxx.")

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        if re.match(r'^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(196[0-9]|197[0-9]|198[0-9]|199[0-9]|200[0-7])$', value):
            self.__birth_date = value
        else:
            raise ValueError("Дата рождения должна быть в формате дд.мм.гггг (день 01-31, месяц 01-12, год 1960-2007).")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if re.match(r'^[a-zA-Z0-9._-]{2,20}@[a-zA-Z]{4,7}\.[a-zA-Z]{2,4}$', value):
            self.__email = value
        else:
            raise ValueError("Email должен содержать буквы, цифры, _-., @, домен 4-7 букв, . и 2-4 буквы.")

    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self, value):
        if re.match(r'^[a-zA-Z]{4,20}$', value):
            self.__specialty = value
        else:
            raise ValueError("Специальность должна состоять только из букв, 4-20 символов.")

    def calculateAge(self):
        # Публичный метод, пока pass
        pass

    def _calculateSalary(self):
        # Защищенный метод, pass
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, phone, birth_date, email, specialty, hours_worked, hourly_rate):
        super().__init__(name, phone, birth_date, email, specialty)
        self.hours_worked = hours_worked  # Вызывает setter
        self.hourly_rate = hourly_rate

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__hours_worked = value
        else:
            raise ValueError("Часы должны быть неотрицательным числом.")

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__hourly_rate = value
        else:
            raise ValueError("Ставка должна быть положительным числом.")

    def _calculateSalary(self):
        return self.__hours_worked * self.__hourly_rate

class SalaryEmployee(Employee):
    def __init__(self, name, phone, birth_date, email, specialty, monthly_salary):
        super().__init__(name, phone, birth_date, email, specialty)
        self.monthly_salary = monthly_salary  # Вызывает setter

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__monthly_salary = value
        else:
            raise ValueError("Зарплата должна быть положительным числом.")

    def _calculateSalary(self):
        return self.__monthly_salary