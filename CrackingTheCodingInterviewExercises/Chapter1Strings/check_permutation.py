'''
Given 2 strings, write a method to decide if one is a permutation of the other.

A permutation is defined as 2 strings containing the same set of characters. Again
always check/clarify with interviewer if case of letters matters, if there may be white space
or other characters that may be ignored.

One easy check - length of the strings - if they are different lengths they are not permutations
'''

# initial solution - count the characters into dictionaries and compare
def get_letter_count(somestring):
    '''get individual letters in each string'''
    temp_alph = {}
    for letter in somestring:
        if letter in temp_alph.keys():
            temp_alph[letter] = temp_alph[letter] + 1
        else:
            temp_alph[letter] = 1
    return temp_alph


def is_permutation(str1, str2):
    '''given two strings determine if they are permutations of each other'''
    if len(str1) != len(str2):
        print "not permutation"
        return False
    temp_alph1 = get_letter_count(str1)
    temp_alph2 = get_letter_count(str2)

    for each in temp_alph1.keys():
        if each in temp_alph2.keys():
            if temp_alph1[each] != temp_alph2[each]:
                print temp_alph1[each], temp_alph2[each]
                print "not permutation"
                return False
        elif each not in temp_alph2.keys():
            print "not permutation"
            return False
    # if we get to this point in the code --> they are permutations
    print "is permutation"
    return True

test_str1 = 'Cat'
test_str2 = 'Tac'
test_str3 = 'cat'
test_str4 = 'tac'
test_str5 = 'bat'
test_str6 = 'tab'


# here I am assume there is a difference between capitals... will add an ignore case
is_permutation(test_str1, test_str2)
is_permutation(test_str2, test_str4)
is_permutation(test_str3, test_str4)
is_permutation(test_str5, test_str6)
