class Bachelor:
    def __init__(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark

    def getScholarship(self):
        if self.averageMark == 5:
            return 10000
        elif self.averageMark > 3:
            return 5000
        else:
            return 0


class Undergraduate(Bachelor):
    def getScholarship(self):
        if self.averageMark == 5:
            return 15000
        elif self.averageMark > 3:
            return 7500
        else:
            return 0


# Пример использования
students = [
    Bachelor("Иван", "Иванов", "Б-101", 5),
    Bachelor("Мария", "Петрова", "Б-102", 4),
    Undergraduate("Алексей", "Сидоров", "М-201", 5),
    Undergraduate("Елена", "Кузнецова", "М-202", 3.5),
    Bachelor("Дмитрий", "Смирнов", "Б-103", 2.8)
]

for student in students:
    print(f"{student.firstName} {student.lastName}: {student.getScholarship()} руб.")