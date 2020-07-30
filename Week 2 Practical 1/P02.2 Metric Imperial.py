#Units Converter

#Take first user inputs
print('***IMPERIAL AND METRIC CONVERTER***')
request=input('Enter W for Weight, D for Distance, L for Liquid>').upper()
conversion=input('Enter I for Imperial -> Metric, M for Metric to Imperial').upper()

#Weights (Stones and Pounds/Kilograms)
if request == 'W':
    if conversion == 'I':

        print('Stones and Pounds to Kilograms Conversion')
        stones = int(input('Stones>'))
        pounds = int(input('Pounds>'))
        total_stones = stones + (pounds/14)
        kg = total_stones * 6.35
        print(kg, 'kgs')
        
    elif conversion == 'M':

        print('Kilograms to Stones and Pounds Conversion')
        kgs = float(input('kgs>'))
        pounds = kgs*2.205
        stones = pounds//14
        print(stones, 'stones and', pounds-(stones*14), 'pounds')
        
    else:
        print('Please enter the correct letter')

#Distances (Miles and Yards/Kilometers and Meters)
elif request == 'D':
    if conversion == 'I':

        print('Miles and Yards to Kilometers and Meters Conversion')
        miles = int(input('Miles>'))
        yards = int(input('Yards>'))
        total_miles = miles + yards/1760
        km = int((total_miles/0.62137)//1)
        meters = ((total_miles/0.62137)%1)* 1000
        print(km, 'km and', meters, 'meters')
        
    elif conversion == 'M':

        print('Kilometers and Meters to Miles and Yards Conversion')
        kilometers = int(input('Kilometers>'))
        meters = int(input('Meters>'))
        total_kilometers = kilometers + meters/1000
        miles = int((total_kilometers/1.609)//1)
        yards = ((total_kilometers/1.609)%1)*1760
        print(miles, 'miles and', yards, 'yards')
        
    else:
        print('Please enter the correct letter')

#Liquids (Gallons and Pints/Litres)
elif request == 'L':
    if conversion == 'I':

        print('Gallons and Pints to Litres Conversion')
        gallons = int(input('Gallons>'))
        pints = int(input('Pints>'))
        total_gallons = gallons + pints/8
        litres = total_gallons*4.546
        print(litres, 'litres')
        
    elif conversion == 'M':

        print('Litres to Gallons and Pints Conversion')
        litres = float(input('Litres>'))
        pints = litres * 1.76
        gallons = pints//8
        print(gallons, 'gallons and', pints-(gallons*8), 'pints')
        
    else:
        print('Please enter the correct letter')

else:
    print('Please enter the correct letter')
