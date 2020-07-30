#Format
#
#key1=>word:frequency,word:frequency,word:frequency
#key2=>word:frequency,word:frequency,word:frequency

def save_user_data(filename, user_dict):

    """Saves user_dict to file name.

    See general format at top.

    Args
        filename: String - Path to save data to.
        user_dict: Dictionary - The data to save.

    """

    f = open(filename, 'a')

    for key in user_dict.keys():
        string_to_write = key+"=>"
        for elem in user_dict[key]:
            string_to_write += elem[0] + ':' + str(elem[1]) + ','
        
        f.write(string_to_write[:-1] + '\n')

    f.close()

def read_from_file(filename):

    """Reads data from filename.

    See general format at top.

    Args
        filename: String - Path to read data from.
    
    Returns
        user_dict: Dictionary - Imported user data.

    Raises
        FileNotFoundError - If filename doesn't exist, prints an error.

    """

    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print("The given file doesn't exist.")
        return ""
    else:
        user_dict = {}
        
        for line in f:
            key_out = line.split("=>")
            this_key = key_out[0]
            user_dict[this_key]=[]

            values = key_out[1].split(',')
            for each in values:
                data = each.split(':')
                user_dict[this_key].append([data[0], int(data[1])])

        f.close()
        return user_dict


user_dict = {'4663':[['home',5],['good',8],['hood',1]],
 '2':[['a',50]]}

save_user_data("P09.7A.txt", user_dict)
print(read_from_file("P09.7A.txt"))