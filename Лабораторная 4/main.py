class Company:
    """ Базовый класс книги. """
    def __init__(self, comp_name: str, location: str):
        """
            Создание и подготовка к работе объекта "Компания"
            :param comp_name: Название компании
            :param location: Местонахождение компании
            Атрибуты comp_name и location изменяться не могут
            Пример:
            >>> comp = Company('ABC', 'Moscow')  #инициализация экземпляра класса
        """

        if not isinstance(comp_name, str):
            raise TypeError("Название компании должно быть типа string")
        self._comp_name = comp_name

        if not isinstance(location, str):
            raise ValueError("Местонахождение компании должно быть типа string")
        self._location = location

    @property
    def comp_name(self):
        return self._comp_name

    @property
    def location(self):
        return self._location

    def __str__(self):
        return f"Название фирмы {self.comp_name}. Местонахождение {self.location}"

    def __repr__(self):
        return f"{self.__class__.__name__}(company_name={self.comp_name!r}, location={self.location!r})"

    def distance(self, current_loc: str) -> bool:
        """
            Функция для проверки возможности доставки товара покупателю

            :param current_loc: Местонахождение покупателя
            :rise TypeError: Местонахождение должно быть типа str.

            :return: Возможна ли доставка

            Пример:
            >>> comp = Company('ABC', 'Moscow')
            >>> comp.distance('Saint Petersburg')
        """
        if not isinstance(current_loc, str):
            raise ValueError("Местонахождение покупателя должно быть типа string")
        self.current_loc = current_loc
        ...

    def salary(self, position: str) -> float:
        """
            Функция для расчета зарплаты сотрудника

            :param position: Должность сотрудника
            :rise TypeError: Должность сотрудника должна быть типа str.

            :return: Зарабатная плата

            Пример:
            >>> comp = Company('ABC', 'Moscow')
            >>> comp.salary('HR')
        """
        if not isinstance(position, str):
            raise ValueError("Должность сотрудника должна быть типа string")
        self.position = position
        ...


class Department(Company):
    def __init__(self, comp_name: str, location: str, department_headcount: int):
        """
            Создание и подготовка к работе объекта "Подразделение компании"
            :param department_headcount: численность сотрудников подразделения
            Примеры:
            >>> comp_dep = Department('ABC', 'Moscow', 15)  #инициализация экземпляра класса
        """
        super().__init__(comp_name, location)

        if not isinstance(department_headcount, int):
            raise TypeError("Количество сотрудников должно быть типа int")
        if department_headcount < 0:
            raise ValueError("Количество сотрудников не может быть отрицательным числом")
        self.department_headcount = department_headcount

    def __str__(self):
        super().__str__()

    def __repr__(self):
        #перегружаем метод, т.к. появился новый атрибут
        return f"{self.__class__.__name__}(comp_name={self.comp_name!r}, location={self.location!r}, department_headcount={self.department_headcount})"

    def distance(self, current_loc: str) -> bool:
        super().distance()

    def salary(self, position: str) -> float:
        """
            Функция для расчета зарплаты сотрудника
            Перегружаем метод, так как руководство отдела может запросить премии и другие выплаты для определенных сотрудников

            :param position: Должность сотрудника
            :rise TypeError: Должность сотрудника должна быть типа str.

            :return: Зарабатная плата

            Пример:
            >>> comp = Company('ABC', 'Moscow')
            >>> comp.salary('HR')
        """
        if not isinstance(position, str):
            raise ValueError("Должность сотрудника должна быть типа string")
        self.position = position
        ...

