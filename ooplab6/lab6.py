from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def createForm(self):
        pass

    @abstractmethod
    def createLabel(self):
        pass

    @abstractmethod
    def createTextBox(self):
        pass

    @abstractmethod
    def createComboBox(self):
        pass

    @abstractmethod
    def createButton(self):
        pass


class WinFactory(AbstractFactory):

    def createForm(self):
        print("For Windows:")
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()


class LinuxFactory(AbstractFactory):
    def createForm(self):
        print("For Linux:")
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()


class MacFactory(AbstractFactory):

    def createForm(self):
        print("For Mac:")
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()


class Control:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def getPos(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Form(Control):
    def __init__(self):
        Control.__init__(self)
        self.controls = []

    def addControl(self, control):
        self.controls.append(control)
        print("Вызван метод addControl у конролла Form")


class Label(Control):
    def __init__(self):
        Control.__init__(self)
        self.text = ""

    def setText(self, text):
        print("Вызван метод setText у конролла Label")
        self.text = text

    def getText(self):
        print("Вызван метод getText у конролла Label")
        return self.text


class TextBox(Control):
    def __init__(self):
        Control.__init__(self)
        self.text = ""

    def setText(self, text):
        print("Вызван метод setText у конролла TextBox")
        self.text = text

    def getText(self):
        print("Вызван метод getText у конролла TextBox")
        return self.text

    def onValueChanged(self):
        print("Вызван метод onValueChanged у конролла TextBox")
        pass


class ComboBox(Control):
    def __init__(self):
        Control.__init__(self)
        self.items = []
        self.selectedIndex = 1

    def setItems(self, items):
        self.items = items
        print("Вызван метод setItems у конролла ComboBox")

    def getItems(self):
        print("Вызван метод getItems у конролла ComboBox")
        return self.items

    def setSelectedIndex(self, selectedIndex):
        self.selectedIndex = selectedIndex
        print("Вызван метод setSelectedIndex у конролла ComboBox")

    def getSelectedIndex(self):
        print("Вызван метод getSelectedIndex у конролла ComboBox")
        return self.selectedIndex


class Button(Control):
    def __init__(self):
        Control.__init__(self)
        self.text = ""

    def setText(self, text):
        self.text = text
        print("Вызван метод setText у конролла Button")

    def getText(self):
        print("Вызван метод getText у конролла Button")
        return self.text

    def click(self):
        print("Вызван метод click у конролла Button")
        pass


print("Выберите платформу")
print("Windows: 1")
print("Linux: 2")
print("MacOS: 3")
choise = input()
if choise == "1":
    factory = WinFactory()
elif choise == "2":
    factory = LinuxFactory()
elif choise == "3":
    factory = MacFactory()
else:
    print("Некорректные данные")

# Создание формы для factory
form = factory.createForm()

# Создание контроллов
Label = factory.createLabel()
Label.setText("Labtext")
print(Label.getText())

TextBox = factory.createTextBox()
TextBox.setText("Text")
print(TextBox.getText())

ComboBox = factory.createComboBox()
ComboBox.setSelectedIndex(1)
ComboBox.setItems(['Item1', 'Item2', 'Item3'])
print(ComboBox.getItems())

Button = factory.createButton()
Button.setText("Buttontext")
print(Button.getText())

# Добавление контроллов на форму
form.addControl(TextBox)
form.addControl(ComboBox)
form.addControl(Label)
form.addControl(Button)
