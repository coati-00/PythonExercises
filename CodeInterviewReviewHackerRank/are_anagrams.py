'''A common question on interviews is to write a function
to tell if two strings are anagrams are one another'''

def get_letter_count(somestring):
    '''get individual letters in each string'''
    temp_alph = {}
    for letter in somestring:
        if letter in temp_alph.keys():
            temp_alph[letter] = temp_alph[letter] + 1
        else:
            temp_alph[letter] = 1
        print temp_alph
    return temp_alph

def are_anagrams(str1, str2):
    '''given two strings determine if they are anagrams'''
    temp_alph1 = get_letter_count(str1)
    temp_alph2 = get_letter_count(str2)
    
    for each in temp_alph1.keys():
        if each in temp_alph2.keys():
            if temp_alph1[each] != temp_alph2[each]:
                print temp_alph1[each], temp_alph2[each]
                print "not anagram"
                return False
        elif each not in temp_alph2.keys():
            print "not anagram"
            return False
    # if we get to this point in the code --> they are anagrams
    print "are anagrams"
    return True
         
            
    

teststr1 = "abcd"
teststr2 = "cdef"
teststr3 = "abcd"
teststr4 = "abcd"



are_anagrams(teststr1, teststr2)
are_anagrams(teststr3, teststr4)





#if __name__ == '__main__':
    

