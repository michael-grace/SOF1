def sum_numbers(a_string):

    """Finds and sums the numbers in a string

    Splits the string at spaces, and loops through this list to add
    the integer value of the element to sum.

    Args
        a_string: String - For the function to find numbers in

    Returns
        sum: Int - The sum of the values in the string

    Raises:
        ValueError: Prints error message if it can't convert to int
            i.e. the string contains a letter. This also returns "Error"
    """

    list_of_numbers = a_string.split(' ')
    sum = 0

    try:
        for i in list_of_numbers:
            sum += int(i)
    
    except ValueError:
        print("You have a bad input file, ensure it contains just numbers.")
        return "Error"
    
    else:
         return sum



def sum_from_file(filename):

    """Opens file, and sums the line totals.

    Attempts to open filename, and loops through each row, and calls
    sum_numbers()

    Args:
        filename: String - The file for the file to open.

    Returns:
        total_sum: Int - The sum of all the lines in the file.

    Raises
        FileNotFoundError: Prints an error if the given filename doesn't
            exist.

        TypeError: Happens if sum_numbers() returns "Error", if it can't
            convert to int. Passes, but ensures the file is closed.
    """

    try:
        f = open(filename, 'r')
    
    except FileNotFoundError:
        print("The Given Filename Doesn't Exist.")
    
    else:
        total_sum = 0

        try:
            for i in f:
                total_sum += sum_numbers(i)
        
        except TypeError:
            pass
        
        else:
            return total_sum
        
        finally:
            f.close()  

print("Sum is: {}".format(sum_from_file('P09.6A.txt')))