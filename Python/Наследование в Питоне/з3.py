class Product:
    def __init__(self, name="", price=0.0, weight=0.0):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight


class Buy(Product):
    def __init__(self, name="", price=0.0, weight=0.0, quantity=0):
        super().__init__(name, price, weight)
        self.__quantity = quantity
        self.__total_price = 0.0
        self.__total_weight = 0.0
        self.__calculate()

    def __calculate(self):
        self.__total_price = self.get_price() * self.__quantity
        self.__total_weight = self.get_weight() * self.__quantity

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity
        self.__calculate()

    def get_total_price(self):
        return self.__total_price

    def get_total_weight(self):
        return self.__total_weight


class Check(Buy):
    def show_info(self):
        print(f"Товар: {self.get_name()}")
        print(f"Цена за штуку: {self.get_price()} руб.")
        print(f"Вес за штуку: {self.get_weight()} кг")
        print(f"Количество: {self.get_quantity()} шт.")
        print(f"Общая цена: {self.get_total_price()} руб.")
        print(f"Общий вес: {self.get_total_weight()} кг")
        print("-" * 30)


# Пример использования
if __name__ == "__main__":
    product1 = Check("Яблоки", 50.0, 0.2, 10)
    product2 = Check("Молоко", 80.0, 1.0, 2)

    product1.show_info()
    product2.show_info()