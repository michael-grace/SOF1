def wildcard_pattern(string, char):
    
    def dowildcard(string, char, thelist):
        """Returns all possible binary values based on wildcards

        Args
            string: String of binary number
            char: String of which character counts as wildcard
                thelist: INTERNAL - The already found values, which can be 
                    added to and  acted on
        
        Returns
            dowildcard(): Recalls the recursive function
            thelist: Base Case - the list of all values found from this version
        """

        if len(string)==0:
            return thelist

        elif (string[0] == '1') or (string[0] == '0'):

            if len(thelist) == 0:
                thelist.append(string[0])
            else:
                for i in range(len(thelist)):
                    thelist[i] += string[0]
            
            return dowildcard(string[1:], char, thelist)

        elif string[0] == char:

            if len(thelist) == 0:
                thelist.append('0')
                thelist.append('1')
            else:
                for i in range(len(thelist)):
                    thelist.append(thelist[i]+'0')
                    thelist[i]+='1'
            
            return dowildcard(string[1:], char, thelist)
    
    values = dowildcard(string, char, [])
    return set(values) if values != [] else {''}


def allwords(digits, keypad):
    def doallwords(digits,keypad,thelist):
        """Returns all possible words from T9 Keypad given the input digits

        Args:
            digits - String of the digits typed in
            keypad - Dictionary of key:list of letter combinations
            thelist - INTERNAL - the list of words already found that can be
                added to or modified

        Returns:
            [x.upper() for x in the list] - list of possible words in capitals
            doallwords... recalling the recursive function

        Raises:
            ValueError - if one of the digits isn't in the 2-9 range
        """
        
        if len(digits)==0:
            return [x.upper() for x in thelist]
        else:
            if int(digits[0]) in range(2,10):
                
                if thelist == []:
                    thelist.extend((keypad[digits[0]]))
                    
                else:
                    for i in range(len(thelist)):
                        temp = thelist[0]
                        thelist.pop(0)
                        for j in range(len(keypad[digits[0]])):
                            thelist.append((temp+keypad[digits[0]][j]).upper())
            else:
                raise ValueError
                

            return (doallwords(digits[1:],keypad,thelist))
    

    values = doallwords(digits,keypad,[])
    return set(values) if values != [] else {''}

def fill_bag(limit, value, weight):
    def currentbag(limit, value, weight, bag):

        if (value==[]) and (weight==[]):
            return bag
        else:
            max_index = value.index(max(value))
            if weight[max_index] > limit:
                weight.pop(max_index)
                value.pop(max_index)
                return currentbag(limit, value, weight, bag)
            else:
                bag.append([value[max_index], weight[max_index]])
                gone = weight.pop(max_index)
                value.pop(max_index)
                return currentbag(limit-gone, value, weight, bag)  
    
    bag = currentbag(limit, value, weight, [])
    total = 0
    for i in bag:
        total += i[1]
    return total    

print(fill_bag(10, [5,4,3,2,1], [1,2,3,4,5]))