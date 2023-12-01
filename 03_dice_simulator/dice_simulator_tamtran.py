from random import randint

while True:
    dice_number = input('How many dice would you like to roll? ')

    if dice_number.lower() == 'exit':
        print('Thanks for playing!')
        break
    else:
        try:
            dice_number_int = int(dice_number)
            if dice_number_int < 0:
                raise ValueError
            
            list_roll = []
            
            for i in range(dice_number_int):
                list_roll.append(randint(1,6))
            
            for i in list_roll:               
                if i == list_roll[-1]:
                    print(i)
                else:
                    print(i, end=',')
        except ValueError as e:
            print('Please enter a valid number.')
            continue


