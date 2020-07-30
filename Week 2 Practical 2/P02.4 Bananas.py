# -*- coding: cp1252 -*-
'''Fruit Prices'''

price_bananas = float(input('How many kg of bananas? '))*3
total_price = price_bananas + 4.99

if price_bananas > 50:
    total_price = price_bananas - 1.5

print('Total Price: £{}'.format(round(total_price, 2)))
