"""
checking the cost.py file
"""

from cost import *

user_price_input = int(input('How much is the cost?\n'))

print ("Where does the cost blong to? \n 1.Complex \n 2.Block \n 3.Floor \n 4.Unit")

user_title_input = int(input("Enter the option's code: \n"))

if (user_title_input == 1):
    
    price = Complex(user_price_input)
    print(price.show_the_object())


elif (user_title_input == 2):
    
    price = Block(user_price_input)
    print(price.show_the_object())


elif (user_title_input == 3):
    
    price = Floor(user_price_input)
    print(price.show_the_object())


elif (user_title_input == 4):
    
    price = Unit(user_price_input)
    print(price.show_the_object())

else:
    print('Not valid')