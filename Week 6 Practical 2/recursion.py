#ITERATIVE
def is_power_it(a,b):
    
    if a==b:
        return True
    elif (b==1) or (b==0):
        return False
    elif (a==1):
        return True

    while True:

        if a==b:
            return True

        elif a<b:
            return False
        
        else:
            a = a//b


def sum_digits_it(number):
    sum = 0
    for i in str(number):
        if i == '-':
            pass
        else:
            sum += int(i)
    return sum

def rec_sum_it(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


