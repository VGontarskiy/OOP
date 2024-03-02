import math


class Point:
    # Класс для представления точки в трехмерном пространстве

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Vector:
    # Класс для представления вектора в трехмерном пространстве

    def __init__(self, *args):
        if len(args) == 3:
            self.x, self.y, self.z = args
        else:
            raise ValueError("Неправильное количество аргументов")

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return str(self)

    # Операции сложения и вычитания векторов
    def sum(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def diff(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def reverse(self):
        # Получение обратного вектора
        return Vector(-self.x, -self.y, -self.z)

    def normalize(self):
        # Построение единичного вектора
        length = self.length()
        return Vector(self.x / length, self.y / length, self.z / length)

    def dot_product(self, other):
        # Скалярное произведение векторов
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        # Векторное произведение векторов
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def mixed_product(self, other1, other2):
        # Смешанное произведение векторов
        return self.dot_product(other1.cross_product(other2))

    def length(self):
        # Длина вектора
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def are_collinear(self, other):
        # Проверка коллинеарности двух векторов
        return self.cross_product(other).length() == 0

    def are_coplanar(self, other1, other2):
        # Проверка компланарности трех векторов
        return self.mixed_product(other1, other2) == 0

    def distance(self, other):
        # Расстояние между двумя векторами
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def angle(self, other):
        # Угол между двумя векторами в радианах
        dot_product = self.dot_product(other)
        magnitude_product = self.length() * other.length()
        if magnitude_product == 0:
            raise ValueError("Невозможно вычислить угол для нулевого вектора")
        return math.acos(dot_product / magnitude_product)


def get_vector_input():
    # Функция для создания вектора
    x, y, z = (map(float, input("Введите координаты вектора (x y z): ").split()))
    return Vector(x, y, z)


x1, y1, z1 = map(float, input("Введите координаты точки 1 (x y z): ").split())
point1 = Point(x1, y1, z1)

x2, y2, z2 = map(float, input("Введите координаты точки 2 (x y z): ").split())
point2 = Point(x2, y2, z2)

print("Введите координаты векторов:")
vector1 = get_vector_input()
vector2 = get_vector_input()

print("Выберите операцию:")
print("1. Сложение векторов")
print("2. Вычитание векторов")
print("3. Обратный вектор")
print("4. Единичный вектор")
print("5. Скалярное произведение векторов")
print("6. Векторное произведение векторов")
print("7. Смешанное произведение векторов")
print("8. Длина вектора")
print("9. Проверка коллинеарности векторов")
print("10. Проверка компланарности векторов")
print("11. Расстояние между точками")
print("12. Угол между векторами")

choice = int(input("Введите номер операции: "))

match choice:
    case 1:
        result = vector1.sum(vector2)
    case 2:
        result = vector1.diff(vector2)
    case 3:
        result = vector1.reverse()
    case 4:
        result = vector1.normalize()
    case 5:
        result = vector1.dot_product(vector2)
    case 6:
        result = vector1.cross_product(vector2)
    case 7:
        result = vector1.mixed_product(vector2, Vector(1, 1, 1))
    case 8:
        result = vector1.length()
    case 9:
        result = vector1.are_collinear(vector2)
    case 10:
        result = vector1.are_coplanar(vector2, Vector(2, 2, 2))
    case 11:
        result = vector1.distance(vector2)
    case 12:
        result = vector1.angle(vector2)
    case _:
        print("Некорректный выбор операции.")
        result = None

if result is not None:
    print(f"Результат операции: {result}")
