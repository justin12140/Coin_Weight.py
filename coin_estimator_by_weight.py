# Coin_Estimator_By_Weight.py
# Created by justin12140

import math

grams_dict = {
    'penny' : 2.5,
    'nickle': 5,
    'dime': 2.268,
    'quarter' : 5.67,
    'penny_dime_limit' : 50,
    'nickle_quarter_limit' : 40 
                    }
    
    
def pound_converstion(unit):
    converted_unit = unit * 0.00220462
    return converted_unit
    
    
def clean_input():
    user_input = int(input('>').strip())
    return user_input


def coin_check(coin_type, coin_weight, coin_limit):
    while True:
        print('What is the weight of the ' + coin_type.title() + ' you have?')
        clean_input()
        if clean_input() > 0:
            total_wrapped = math.ceil(((clean_input() / coin_weight) / coin_limit))
            print("You have a total of ", int(clean_input() // coin_weight),' ', coin_type.title(),
                  " which can be placed in %d wrappings!" % total_wrapped)
            break

        else:
            print("That is not a valid value! Please try again.")

            
print('This program will take the weight of the coins you have, and tell you how many wrappers you can fit.')
print('Would you like to submit weight in pounds or grams?')

while True:
    weight_type = input('> ')
    if weight_type.strip() == 'pounds' or weight_type.strip() == 'Pounds':
        coin_check('pennies', pound_converstion( grams_dict['penny']), grams_dict['penny_dime_limit'])
        coin_check('nickles', pound_converstion( grams_dict['nickle']),grams_dict['nickle_quarter_limit'])
        coin_check('dimes', pound_converstion( grams_dict['dime']),grams_dict['penny_dime_limit'])
        coin_check('quarters',pound_converstion( grams_dict['quarter']), grams_dict['nickle_quarter_limit'])
        break
    elif weight_type.strip() == 'grams' or weight_type.strip() == 'Grams':
        coin_check('pennies', grams_dict['penny'], grams_dict['penny_dime_limit'])
        coin_check('nickles', grams_dict['nickle'], grams_dict['nickle_quarter_limit'])
        coin_check('dimes', grams_dict['dime'], grams_dict['penny_dime_limit'])
        coin_check('quarters', grams_dict['quarter'], grams_dict['nickle_quarter_limit'])
        break
    else:
        print("This is not a valid entry. Please try again.")

