'''Area of a Triangle'''

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

area = 0.25*((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))**0.5
print('Area: {}'.format(area))
