class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.isalpha():
            raise ValueError("Некорректное имя")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or not (0 <= value <= 110):
            raise ValueError("Некорректный возраст")
        self.__age = value

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not isinstance(new_name, str) or not new_name.isalpha():
            raise ValueError("Некорректное имя")
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if not isinstance(new_age, int) or not (0 <= new_age <= 110):
            raise ValueError("Некорректный возраст")
        self.__age = new_age


# Пример использования
user = User('Гвидо', 65)
print(user.name)
print(user.age)