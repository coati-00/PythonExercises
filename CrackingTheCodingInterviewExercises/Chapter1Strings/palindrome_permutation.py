'''
Given a string determine if it is a palindrome... regardless of whether it is a dictionary word or not.

So in order for it to be possible to arrange a string the same forwards in backwards:
1 - strings with an odd number of characters can only have 1 letter in the middle,
all other letters must be of an even number
2- strings with an even number of characters, all characters must be of an even number

'''

# not palindromes
teststr1 = "abcd"
teststr2 = "cdef"
teststr3 = "abcdef"
teststr4 = "abcdefghi"

# palindromes some actual words, others not
teststr5 = "abcdedcba"
teststr6 = "radar"
teststr7 = "level"
teststr8 = "civic"



def get_letter_count(somestring):
    '''get individual letters in each string'''
    temp_alph = {}
    for letter in somestring:
        if letter in temp_alph.keys():
            temp_alph[letter] = temp_alph[letter] + 1
        else:
            temp_alph[letter] = 1
    return temp_alph

def is_even(something):
    '''I assume I am working with strings and ints in this script'''
    if type(something) is int:
        if something % 2 == 0:
            return True
        elif something % 2 == 1:
            return False
    if type(something) is str:
        count = len(something)
        if count % 2 == 0:
            return True
        elif count % 2 == 1:
            return False

def is_palindrome_permutation(somestring):
    '''determine if string could be arranged as a palindrome'''
    letter_check = get_letter_count(somestring)
    if is_even(somestring):
        '''if the string has an even number of letters any that do
        not have an even count make it not a palindrome'''
        for each in letter_check.keys():
            if not is_even(letter_check[each]):
                print "is not a palindrome"
                return False
    if not is_even(somestring):
        '''if the string has an odd length it will have one letter
        that has an odd count, but no more than that's it'''
        count_odd = 0
        for each in letter_check.keys():
            if count_odd > 1:
                print "is not a palindrome"
                return False
            if not is_even(letter_check[each]):
                count_odd = count_odd + 1
        # if we get to this point in the code --> could be palindrome
        print "could be palindrome"
        return True


is_palindrome_permutation(teststr1)
is_palindrome_permutation(teststr2)
is_palindrome_permutation(teststr3)
is_palindrome_permutation(teststr4)
is_palindrome_permutation(teststr5)
is_palindrome_permutation(teststr6)
is_palindrome_permutation(teststr7)
is_palindrome_permutation(teststr8)