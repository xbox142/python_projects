import random

name = input('What is your name? >> ')
print(f'Welcome to hangman, {name}!')

word_list = ['apple','secret','banana']

word = random.choice(word_list)
print('Word: ' + '_'*len(word))

tries = 3
guessed = ''

while tries > 0:
    blank = 0
    l = input('\nEnter a letter: ')
    if l not in word:
        tries -= 1
        print(f'There is not any letter! There are {tries} left')
    else:
        if l in guessed:
            print('The letter was selected!')
        else:
            guessed += l
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('x', end='')
                blank += 1
        continue

if blank == 0:
    print('You win!')
else:
    print('You lose!')