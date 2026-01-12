class Father:
    def __init__(self, mood="neutral"):
        self.mood = mood

    def greet(self):
        return "Hello!"

    def be_strict(self):
        self.mood = "strict"


class Mother:
    def __init__(self, mood="neutral"):
        self.mood = mood

    def greet(self):
        return "Hi, honey!"

    def be_kind(self):
        self.mood = "kind"


class Daughter(Father, Mother):
    def __init__(self, mood="neutral"):
        super().__init__(mood)

    def greet(self):
        return Mother.greet(self)


class Son(Father, Mother):
    def __init__(self, mood="neutral"):
        super().__init__(mood)

    def greet(self):
        return Father.greet(self)


# Проверка
if __name__ == "__main__":
    print("=== Проверка класса Father ===")
    father = Father()
    print("father.mood (по умолчанию): " + father.mood)
    print("father.greet(): " + father.greet())
    father.be_strict()
    print("father.mood после be_strict(): " + father.mood)

    print("\n=== Проверка класса Mother ===")
    mother = Mother()
    print("mother.mood (по умолчанию): " + mother.mood)
    print("mother.greet(): " + mother.greet())
    mother.be_kind()
    print("mother.mood после be_kind(): " + mother.mood)

    print("\n=== Проверка класса Daughter ===")
    daughter = Daughter()
    print("daughter.mood (по умолчанию): " + daughter.mood)
    print("daughter.greet(): " + daughter.greet())  # Должно быть от Mother
    daughter.be_kind()
    print("daughter.mood после be_kind(): " + daughter.mood)
    daughter.be_strict()
    print("daughter.mood после be_strict(): " + daughter.mood)

    print("\n=== Проверка класса Son ===")
    son = Son()
    print("son.mood (по умолчанию): " + son.mood)
    print("son.greet(): " + son.greet())  # Должно быть от Father
    son.be_kind()
    print("son.mood после be_kind(): " + son.mood)
    son.be_strict()
    print("son.mood после be_strict(): " + son.mood)