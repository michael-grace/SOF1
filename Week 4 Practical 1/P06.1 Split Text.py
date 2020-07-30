#***Split Text***

import copy

sample_text = "As Python's creator, I'd like to say a few words about its origins."

'''
1) Loop through letters
2) If not a letter, remove front of copy of the text to list
'''

def split_text(sample_text):
    sample_text_2 = copy.copy(sample_text)
    split_list = []
    

    for i in sample_text:

        if (not i.isalpha()) and len(sample_text_2[:sample_text_2.index(i)])!=0:
            split_list.append(sample_text_2[:sample_text_2.index(i)])
            sample_text_2 = sample_text_2[sample_text_2.index(i)+1:] 
        elif (not i.isalpha()):
            sample_text_2 = sample_text_2[1:]

    return split_list

print(split_text(sample_text))
