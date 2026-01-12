from datetime import date

class BirthInfo:
    def __init__(self, birth_date):
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif isinstance(birth_date, str):
            try:
                year, month, day = map(int, birth_date.split('-'))
                self.birth_date = date(year, month, day)
            except (ValueError, TypeError):
                raise TypeError("Аргумент переданного типа не поддерживается")
        elif isinstance(birth_date, (list, tuple)) and len(birth_date) == 3:
            try:
                year, month, day = map(int, birth_date)
                self.birth_date = date(year, month, day)
            except (ValueError, TypeError):
                raise TypeError("Аргумент переданного типа не поддерживается")
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age


# Примеры использования:
birthinfo1 = BirthInfo(date(2023, 2, 26))
print(birthinfo1.age)

birthinfo2 = BirthInfo('2023-02-26')
print(birthinfo2.age)

birthinfo3 = BirthInfo([2023, 2, 26])
print(birthinfo3.age)