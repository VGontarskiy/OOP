import numpy as np


class Integral:
    def __init__(self, function, down, up, num):
        self.function = function
        self.down = down
        self.up = up
        self.num = num

    def Calc(self):
        pass


# Метод Симпсона
class Simp(Integral):
    def Calc(self):
        h = (self.up - self.down) / self.num
        result = self.function(self.down) + self.function(self.up)

        for i in range(1, self.num):
            x_i = self.down + i * h
            result += 4 * self.function(x_i) if i % 2 == 1 else 2 * self.function(x_i)

        return h * result / 3


# Метод Трапеции
class Trap(Integral):
    def Calc(self):
        total = 0
        array = np.linspace(self.down, self.up, self.num)
        for i in array:
            total += 2 * self.function(i)
        result = (array[1] - array[0]) * (total - self.function(array[0]) - self.function(array[-1])) / 2
        return result


# Подынтегральная функция
def func(x):
    return x ** 4


print(f"Метод Сипсона: {Simp(func, 0, 1, 1000).Calc()}")
print(f"Метод Трапеций: {Trap(func, 0, 1, 1000).Calc()}")
