#RECURSIVE
def is_power(a,b):
    def power_function(a,b,numbers):
        print(a, b)
        if a==b:
            return True

        elif b==1:
            return False

        elif (a==1) and (b==0):
            return False
        elif (a==1) and (numbers == [a,b]):
            return True

        elif b==0:
            return False

        elif a<b:
            return False

        else:
            return power_function(a//b, b, numbers)
    return power_function(a,b,[a,b])

def sum_digits(number):
    def sum_function(number, sum):
        if str(number)[-1]=='-':
            pass
        else:
            sum += int(str(number)[-1])

        if len(str(number)[:-1]) == 0:
            return sum
        else:
            return sum_function(str(number)[:-1], sum)

    return sum_function(number, 0)


def rec_sum(numbers):
    def summing(numbers, sum):
        if len(numbers)==1:
            return (sum + numbers[0])
        elif len(numbers)==0:
            return 0
        else:
            sum += numbers.pop()
            print(sum, numbers)
            return summing(numbers, sum)
    return summing(numbers, 0)

def iselfish(word):
    def test_elfish(word, results):
        if len(word)==0:
            return not(False in results.values())     
        else:
            test_letter = word[-1]
            if test_letter in results.keys():
                results[test_letter] = True

            return test_elfish(word[:-1], results)
    return test_elfish(word, {'e':False, 'l':False, 'f':False})

#for i in ['whiteleaf', 'tasteful', 'unfriendly', 'and', 'waffles']:
#    print(iselfish(i))

def flatten(mlist):
    def do_flattening(mlist, output):
        
        if len(mlist) == 0:
            return output
        else:
            if type(mlist[0]) == list:
                output.extend(do_flattening(mlist[0], []))
            else:
                output.append(mlist[0])
            mlist.pop(0)
            return do_flattening(mlist, output)


        
        
    return do_flattening(mlist, [])

def merge(sorted_listA, sorted_listB):
    def do_merge(listA, listB, output):
        if (len(listA) == 0) and (len(listB)==0):
            return output
        elif len(listA)==0:
            output.append(listB[0])
            listB.pop(0)
            do_merge([], listB, output)
        elif len(listB)==0:
            output.append(listA[0])
            listA.pop(0)
            do_merge(listA, [], output)
        else:
            if listA[0]<listB[0]:
                output.append(listA[0])
                listA.pop(0)
            elif listB[0]<listA[0]:
                output.append(listB[0])
                listB.pop(0)
            else:
                output.extend([listA[0], listB[0]])
                listA.pop(0)
                listB.pop(0)
            
        return do_merge(listA, listB, output)
    return do_merge(sorted_listA, sorted_listB, [])

