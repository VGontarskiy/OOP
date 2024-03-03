class Control:
    def setPosition(self, x, y):
        print(f"Установка позиции по ({x}, {y})")

    def getPosition(self):
        print("Получение позиции")


# Создание класса-фабрики для генерации контролов
class ControlFactory:
    def createForm(self):
        pass

    def createLabel(self):
        pass

    def createTextBox(self):
        pass

    def createComboBox(self):
        pass

    def createButton(self):
        pass


# Создание классов контролов для различных операционных систем
class WindowsControlFactory(ControlFactory):
    def createForm(self):
        return WindowsForm()

    def createLabel(self):
        return WindowsLabel()

    def createTextBox(self):
        return WindowsTextBox()

    def createComboBox(self):
        return WindowsComboBox()

    def createButton(self):
        return WindowsButton()


class LinuxControlFactory(ControlFactory):
    def createForm(self):
        return LinuxForm()

    def createLabel(self):
        return LinuxLabel()

    def createTextBox(self):
        return LinuxTextBox()

    def createComboBox(self):
        return LinuxComboBox()

    def createButton(self):
        return LinuxButton()


class MacOSControlFactory(ControlFactory):
    def createForm(self):
        return MacOSForm()

    def createLabel(self):
        return MacOSLabel()

    def createTextBox(self):
        return MacOSTextBox()

    def createComboBox(self):
        return MacOSComboBox()

    def createButton(self):
        return MacOSButton()


# Создание классов контролов для каждой операционной системы
# Windows \\\\\\\\\\
class WindowsForm(Control):
    def addControl(self, control):
        print(f"Добавление контролла Control в форму Windows")


class WindowsLabel(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для метки Windows")

    def getText(self):
        print("Получение текста из метки Windows")


class WindowsTextBox(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для текстового поля Windows")

    def getText(self):
        print("Получение текста из текстового поля Windows")

    def onValueChanged(self):
        print("Событие OnValueChanged для текстового поля Windows")


class WindowsComboBox(Control):
    def setSelectedIndex(self, index):
        print(f"Установка выбранного индекса {index} для комбинированного поля Windows")

    def getSelectedIndex(self):
        print("Получение выбранного индекса из комбинированного поля Windows")

    def setItems(self, items):
        print(f"Установка элементов {items} для комбинированного поля Windows")

    def getItems(self):
        print("Получение элементов из комбинированного поля Windows")


class WindowsButton(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для кнопки Windows")

    def getText(self):
        print("Получение текста из кнопки Windows")

    def click(self):
        print("Событие клика для кнопки Windows")


# Linux \\\\\\\\\\
class LinuxForm(Control):
    def addControl(self, control):
        print(f"Добавление контролла Control в форму Linux")


class LinuxLabel(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для метки Linux")

    def getText(self):
        print("Получение текста из метки Linux")


class LinuxTextBox(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для текстового поля Linux")

    def getText(self):
        print("Получение текста из текстового поля Linux")

    def onValueChanged(self):
        print("Событие OnValueChanged для текстового поля Linux")


class LinuxComboBox(Control):
    def setSelectedIndex(self, index):
        print(f"Установка выбранного индекса {index} для комбинированного поля Linux")

    def getSelectedIndex(self):
        print("Получение выбранного индекса из комбинированного поля Linux")

    def setItems(self, items):
        print(f"Установка элементов {items} для комбинированного поля Linux")

    def getItems(self):
        print("Получение элементов из комбинированного поля Linux")


class LinuxButton(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для кнопки Linux")

    def getText(self):
        print("Получение текста из кнопки Linux")

    def click(self):
        print("Событие клика для кнопки Linux")


# MacOS \\\\\\\\\\
class MacOSForm(Control):
    def addControl(self, control):
        print(f"Добавление контролла Control в форму MacOS")


class MacOSLabel(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для метки MacOS")

    def getText(self):
        print("Получение текста из метки MacOS")


class MacOSTextBox(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для текстового поля MacOS")

    def getText(self):
        print("Получение текста из текстового поля MacOS")

    def onValueChanged(self):
        print("Событие OnValueChanged для текстового поля MacOS")


class MacOSComboBox(Control):
    def setSelectedIndex(self, index):
        print(f"Установка выбранного индекса {index} для комбинированного поля MacOS")

    def getSelectedIndex(self):
        print("Получение выбранного индекса из комбинированного поля MacOS")

    def setItems(self, items):
        print(f"Установка элементов {items} для комбинированного поля MacOS")

    def getItems(self):
        print("Получение элементов из комбинированного поля MacOS")


class MacOSButton(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для кнопки MacOS")

    def getText(self):
        print("Получение текста из кнопки MacOS")

    def click(self):
        print("Событие клика для кнопки MacOS")


print("Выберите платформу")
print("Windows: 1")
print("Linux: 2")
print("MacOS: 3")
choise = input()
if choise == "1":
    factory = WindowsControlFactory()
elif choise == "2":
    factory = LinuxControlFactory()
elif choise == "3":
    factory = MacOSControlFactory()
else:
    print("Некорректные данные")

# Создание экземпляров контролов для различных операционных систем
Form = factory.createForm()
Label = factory.createLabel()
TextBox = factory.createTextBox()
ComboBox = factory.createComboBox()
Button = factory.createButton()

# Симуляция вызова методов контролов
Form.setPosition(10, 10)
Form.addControl(Label)
Label.setText("Пример текста")
Label.getText()
TextBox.setPosition(20, 20)
TextBox.setText("Введенный текст")
TextBox.getText()
TextBox.onValueChanged()
ComboBox.setPosition(30, 30)
ComboBox.setSelectedIndex(0)
ComboBox.getSelectedIndex()
ComboBox.setItems(["Элемент 1", "Элемент 2"])
ComboBox.getItems()
Button.setPosition(40, 40)
Button.setText("Нажми меня")
Button.getText()
Button.click()