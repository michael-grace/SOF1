number_cakes = int(input('Enter the number of cake(s) you want to buy: '))
cake_price = 2.50
bill = cake_price * number_cakes


if number_cakes == 1:
    print('The price of cake is', bill, 'pounds.')
elif number_cakes < 1:
    print('Error, the number entered is invalid!')
else: #meaning number of cakes >1
    print('The price of', number_cakes, 'cakes is', bill, 'pounds.')



