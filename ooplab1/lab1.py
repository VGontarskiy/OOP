import numpy as np


class Integral:
    def __init__(self, function, down, up):
        self.function = function
        self.down = down
        self.up = up

    def Calc(self):
        pass


# Метод Симпсона
class Simp(Integral):
    def Calc(self):
        return (self.up - self.down) * (self.function(self.up) + self.function(self.down) + 4 * self.function((self.up + self.down) / 2)) / 6


# Метод Трапеции
class Trap(Integral):
    def Calc(self):
        total = 0
        array = np.linspace(self.down, self.up, 1000)
        for i in array:
            total += 2 * self.function(i)
        result = (array[1] - array[0]) * (total - self.function(array[0]) - self.function(array[-1])) / 2
        return result


# Подынтегральная функция
def func(x):
    return x ** 4


print(f"Метод Сипсона: {Simp(func, 0, 1).Calc()}")
print(f"Метод Трапеций: {Trap(func, 0, 1).Calc()}")
