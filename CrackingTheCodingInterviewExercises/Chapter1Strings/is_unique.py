'''Determine if a string has all unique characters'''

test_str1 = 'Long test string here.'
test_str2 = 'No duplicates'
test_str3 = 'duplication duplication lots of duplication'
test_str4 = 'test'
test_str5 = 'test test'
test_str6 = 'something'



# using external data structure
def get_letter_count(somestring):
    '''get individual letters in each string'''
    temp_alph = {}
    for letter in somestring:
        if letter in temp_alph.keys():
            temp_alph[letter] = temp_alph[letter] + 1
        else:
            temp_alph[letter] = 1
    return temp_alph



# without using external data structure
