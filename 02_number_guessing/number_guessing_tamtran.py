from random import randint

number = randint(0,10)

while True:
    try:
        guessing_number = int(input('Please enter the guessing number 0 --> 10: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue

    if guessing_number > number:
        print('Guessing higher')
    elif guessing_number < number:
        print('Guesing lower')
    else:
        print('Great, you guess the number')
        break


