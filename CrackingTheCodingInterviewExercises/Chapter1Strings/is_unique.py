'''
Determine if a string has all unique characters
Clarify what set of characters you are working with - all ascii, extended ascii,
unicode, the 26 A-Z, caps a lowercase, no case etc.
'''



test_str1 = 'Long test string here.'
test_str2 = 'No duplicates'
test_str3 = 'duplication duplication lots of duplication'
test_str4 = 'test'
test_str5 = 'test test'
test_str6 = 'something'


'''Variation 1 - using whatever other structures/functions you want'''
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


def is_unique(somestring):
    '''check if any of the letters occurs more than once'''
    temp_alph = get_letter_count(somestring)

    for each in temp_alph.keys():
        if temp_alph[each] > 1:
                print "not unique"
                return False
    # if we get to this point in the code --> letters are unique
    print "is unique"
    return True

is_unique(test_str1)
is_unique(test_str2)
is_unique(test_str3)
is_unique(test_str4)
is_unique(test_str5)
is_unique(test_str6)


'''
without using external data structure
this is very slow - you need to keep looping
over the string repeatedly comparing each letter to all of the others

approach - loop over string and then get index of current position, compare to all other positions
'''


def is_unique_no_struct(somestring):
    total = len(somestring)
    for each in somestring:
        position = somestring.index(each)
        counter = 0
        while counter < total:
            if counter != position:
                if each == somestring[counter]:
                    print "duplicate letter found - not unique"
                    return False
            counter = counter + 1
    print "characters are unique"
    return True

is_unique_no_struct(test_str1)
is_unique_no_struct(test_str2)
is_unique_no_struct(test_str3)
is_unique_no_struct(test_str4)
is_unique_no_struct(test_str5)
is_unique_no_struct(test_str6)




