import argparse

class Sample():
    pass

class Dog():
    species = 'Mammal'

    def __init__(self,mybreed, myname, spots):
        self.breed = mybreed
        self.name = myname
        self.spots = spots
    
    def bark(self,n):
        print("Woof! {} {}".format(self.name,n))

class Circle():
    pi = 3.1416
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi
        self.area = radius * radius * Circle.pi

    def get_circunference(self):
        return self.radius * self.pi * 2

class Animal():
    def __init__(self):
        print('Animal Created')
    
    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print('I am eating')
    
    def bark(self):
        print("Woof!")

class Doggie(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Doggie created")

    def who_am_i(self):
        print("I'm doggie")

class Perro():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print('Book deleted')
    

def get_args():
    parser = argparse.ArgumentParser(description='Bottles of beer song',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n','--num',metavar='number',type=int,default=10,help='How many bottles')
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def main():
    print('OO1')
    my_sample = Sample()
    print(type(my_sample))

    my_dog = Dog(mybreed='Huskie',myname='Manchitas',spots=False)
    print(type(my_dog))
    print(my_dog.breed)

    print(my_dog.species)
    my_dog.bark(100)

    my_circle = Circle(30)
    print(my_circle.get_circunference())
    print(my_circle.area)

    my_doggie = Doggie()
    my_doggie.eat()
    my_doggie.who_am_i()
    my_doggie.bark()

    niko = Perro("niko")
    felix = Cat("felix")
    print(niko.speak())
    print(felix.speak())

    b = Book('Hello','Felipe',100)
    print(str(b))
    print(len(b))
    del b

if __name__ == '__main__':
    main()

