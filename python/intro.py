import random

print('Hello, What is your favorite number?')
number = input();

print('your favorite number is ' + number)

minNumber = 1
maxNumber = 10
magicNumber = random.randint(minNumber, maxNumber)

message = 'the magic number is between {0} and {1}'
print(message.format(minNumber, maxNumber))

found = False
while not found:
    print('Guess what it is')
    guess = int (input())
    if guess == magicNumber:
        found = True
    if guess < magicNumber:
        print('too low')
    if guess > magicNumber:
        print('too high')
print('You Got it!, ')
