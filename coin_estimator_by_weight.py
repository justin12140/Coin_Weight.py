# Coin_Estimator_By_Weight.py
# Created by justin12140

import math

print('This program will take the weight of the coins you have, and tell you how many wrappers you can fit.')
print('Would you like to submit weight in pounds or grams?')

x = 0
coins = ['pennies', 'nickles','dimes', 'quarters']
pound_conversion = 0.00220462
pennies_grams = 2.5
pennies_pounds = pennies_grams * pound_conversion
pennies_limit = 50
nickles_grams = 5
nickles_pounds = nickles_grams * pound_conversion
nickles_limit = 40
dimes_grams = 2.268
dimes_pounds = dimes_grams * pound_conversion
dimes_limit = 50
quarters_grams = 5.67
quarters_pounds = quarters_grams * pound_conversion
quarters_limit = 40

final_weight = 'Unresolved'
def coin_check(coin_type, coin_weight, coin_limit):
    global final_weight
    final_weight = 'Unresolved'
    while final_weight == 'Unresolved':
        print('What is the weight of the ' + coin_type.title() + ' you have?')
        user_input = int(input('> '))
        if str(user_input).strip().isdigit() == True and user_input != 0:
            total_wrapped = math.ceil(((user_input / coin_weight)/coin_limit))
            print("You have a total of " + str(int(user_input//coin_weight)) + ' ' + coin_type.title() +
                  " which can be placed in %d wrappings!" %total_wrapped)
            final_weight = "Resolved"
        else:
            print("That is not a valid value! Please try again.")

while x == 0:
    weight_type = input('> ')
    if weight_type.strip() == 'pounds' or weight_type.strip() == 'Pounds':
        coin_check('pennies',pennies_pounds,pennies_limit)
        coin_check('nickles', nickles_pounds,nickles_limit)
        coin_check('dimes', dimes_pounds,dimes_limit)
        coin_check('quarters',quarters_pounds, quarters_limit)
        x = 1
    elif weight_type.strip() == 'grams' or weight_type.strip() == 'Grams':
        coin_check('pennies', pennies_grams, pennies_limit)
        coin_check('nickles', nickles_grams, nickles_limit)
        coin_check('dimes', dimes_grams, dimes_limit)
        coin_check('quarters', quarters_grams, quarters_limit)
        x = 1
    else:
        print("This is not a valid entry. Please try again.")

