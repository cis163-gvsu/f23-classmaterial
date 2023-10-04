class Pet:

    def __init__(self, name, weight, breed, age):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.age = age

    def print_name(self):
        print(f"Animal's name is {self.name}")

class Dog(Pet):
    def __init__(self, name, weight, breed, age, coat_type):
        self.coat_type = coat_type
        super().__init__(name, weight, breed, age)

    @classmethod
    def bark(cls):
        print('woof woof')
        #print(cls.name) #this fails, no name in class

    def print_name(self):
        print(f"Dog's name is {self.name}")
            

class Cat(Pet):
    count = 0 #class variable
    def __init__(self, name, weight, breed, age):
        self.count = 0
        super().__init__(name, weight, breed, age)

    def meow(self):
        Cat.count += 1
        self.count += 1
        print('meow meow')
        print(f'called meow {Cat.count} times')
        print(f'self.count is {self.count}')

if __name__ == '__main__':
    c1 = Cat('kit', 7, 'siamese', 4)
    c2 = Cat('ezra', 5, 'persian', 6)
    d = Dog('chewie', 30, 'goldendoodle', 7, 'curly')
    c1.print_name()
    c2.print_name()
    d.print_name()
    # Dog.print_name() # this fails because not a classmethod
    c1.meow()
    c2.meow()
    d.bark()
    Dog.bark()

    print(isinstance(d, Dog))
    print(isinstance(d, Pet))
    print(isinstance(c1, Pet))
    print(isinstance(c1, Dog))
