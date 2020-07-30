'''Heart Rates'''

max_rate = 208 - 0.7*int(input('Age: '))
heart_rate = int(input('Heart Rate: '))

if heart_rate >= 0.9*max_rate:
    print('Interval Training')
elif (heart_rate >= 0.7*max_rate) and (heart_rate < 0.9*max_rate):
    print('Threshold Training')
elif (heart_rate >= 0.5*max_rate) and (heart_rate < 0.7*max_rate):
    print('Aerobic Training')
elif heart_rate < 0.9*max_rate:
    print('Couch Potato')
else:
    print('Please enter a valid heart rate')
