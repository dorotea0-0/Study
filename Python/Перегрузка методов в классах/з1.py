class Negator:
    @staticmethod
    def neg(obj):
        if isinstance(obj, (int, float)):
            return -obj
        elif isinstance(obj, bool):
            return not obj
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")

print(Negator.neg(5))
print(Negator.neg(-3.14))
print(Negator.neg(True))
print(Negator.neg(False))