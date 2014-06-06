class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Hello, ', self.name)

p1 = Person('Webster')
p1.say_hello()

p2 = Person('Munoz')
p2.say_hello()
