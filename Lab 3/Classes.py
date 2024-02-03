#1
class Myclass:
    def __init__(self):
        self.string
    def GetString(self):
        self.string = intput()
    def PrintString(self):
        self.string = print(self.string.upper())
x = Myclass()
x.GetString()
x.PrintString()

#2
class Shape:
    def area(self) -> None:
        self.a = 0
    class Square:
        def __init__(self):
            self.length
        def area(self):
            self.a = self.length * self.length
x = Shape()
x.area()