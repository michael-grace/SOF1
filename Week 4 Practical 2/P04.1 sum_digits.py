#***Sum Digits

def sum_digits(number):
    the_string = str(number)
    total = 0
    for i in the_string:
        total += int(i)
    return total

print(sum_digits(1234))