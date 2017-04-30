'''This is a second variation of the anagram question, except instead of
asking you to write a function that tells you if two strings are anagrams
they ask you to tell you how many letters you need to remove to turn the
strings into anagrams... so for example abcd dcfg you would need to remove
a and b from the first string and f and g from the second.'''


def get_letter_count(somestring):
    '''get individual letters in each string'''
    temp_alph = {}
    for letter in somestring:
        if letter in temp_alph.keys():
            temp_alph[letter] = temp_alph[letter] + 1
        else:
            temp_alph[letter] = 1
    return temp_alph

def compare_letters_for_anagrams(str1, str2):
    '''given two strings determine if they are anagrams'''
    temp_alph1 = get_letter_count(str1)
    temp_alph2 = get_letter_count(str2)

    for each in temp_alph1.keys():
        if each in temp_alph2.keys():
            if temp_alph1[each] != temp_alph2[each]:
                print each, temp_alph1[each], each, temp_alph2[each]
        elif each not in temp_alph2.keys():
            print "key in list one " + str1 + " not in list two " + str2
            print each, temp_alph1[each]
    
    for each in temp_alph2.keys():
        if each in temp_alph1.keys():
            if temp_alph2[each] != temp_alph1[each]:
                print each, temp_alph1[each], each, temp_alph2[each]
        elif each not in temp_alph1.keys():
            print "key in list two " + str1 + " not in list one " + str2
            print each, temp_alph2[each]
    

teststr1 = "abcd"
teststr2 = "cdef"
teststr3 = "abcdef"
teststr4 = "abcdefghi"


compare_letters_for_anagrams(teststr1, teststr2)
compare_letters_for_anagrams(teststr1, teststr1)
compare_letters_for_anagrams(teststr3, teststr1)
compare_letters_for_anagrams(teststr1, teststr4)





#if __name__ == '__main__':
    