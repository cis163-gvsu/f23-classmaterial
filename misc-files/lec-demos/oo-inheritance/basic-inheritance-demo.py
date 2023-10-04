class Animal:
    def __init__(self, name):
        self.name = name



class Fish(Animal):
    def __init__(self, name):
        self.x = 0
        self.y = 0
        super().__init__(name)

    def move(self, xchange, ychange):
        self.x += xchange
        self.y += ychange

    def __str__(self):
        temp = self.name
        return f'Fish named {temp} at location ({self.x},{self.y})'


if __name__ == '__main__':
    flounder = Fish('flounder')
    print(flounder)
