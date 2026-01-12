class ChessPiece:
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def can_move(self):
        raise NotImplementedError("Subclasses must implement can_move method")


class King(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)

    def can_move(self, target_horizontal, target_vertical):
        if not ('a' <= target_horizontal <= 'h' and 1 <= target_vertical <= 8):
            return False

        dx = abs(ord(target_horizontal) - ord(self.horizontal))
        dy = abs(target_vertical - self.vertical)

        return (dx <= 1 and dy <= 1) and (dx != 0 or dy != 0)


class Knight(ChessPiece):
    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)

    def can_move(self, target_horizontal, target_vertical):
        if not ('a' <= target_horizontal <= 'h' and 1 <= target_vertical <= 8):
            return False

        dx = abs(ord(target_horizontal) - ord(self.horizontal))
        dy = abs(target_vertical - self.vertical)

        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


print(" Проверка короля ")
king1 = King('e', 4)
print("Король на e4 может пойти на d5? {king1.can_move('d', 5)}")   # True (диагональ)
print("Король на e4 может пойти на e5? {king1.can_move('e', 5)}")   # True (вверх)
print("Король на e4 может пойти на g6? {king1.can_move('g', 6)}")   # False (слишком далеко)
print("Король на e4 может пойти на e4? {king1.can_move('e', 4)}")   # False (не движение)

print("\n Проверка коня ")
knight1 = Knight('b', 1)
print("Конь на b1 может пойти на c3? {knight1.can_move('c', 3)}")   # True (стандартный ход)
print("Конь на b1 может пойти на d2? {knight1.can_move('d', 2)}")   # True (стандартный ход)
print("Конь на b1 может пойти на a3? {knight1.can_move('a', 3)}")   # True (стандартный ход)
print("Конь на b1 может пойти на b2? {knight1.can_move('b', 2)}")   # False (не "Г")
print("Конь на b1 может пойти на c2? {knight1.can_move('c', 2)}")   # False (не "Г")

print("\n Дополнительные проверки ")
king2 = King('a', 1)
print("Король на a1 может пойти на b2? {king2.can_move('b', 2)}")   # True
print("Король на a1 может пойти на a2? {king2.can_move('a', 2)}")   # True
print("Король на a1 может пойти на h8? {king2.can_move('h', 8)}")   # False

knight2 = Knight('e', 4)
print("Конь на e4 может пойти на f6? {knight2.can_move('f', 6)}")   # True
print("Конь на e4 может пойти на d6? {knight2.can_move('d', 6)}")   # True
print("Конь на e4 может пойти на e4? {knight2.can_move('e', 4)}")   # False