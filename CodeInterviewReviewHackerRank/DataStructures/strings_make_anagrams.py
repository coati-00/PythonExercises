'''On HackerRank site anagram question is how many letters must you remove
 to make the 2 strings anagrams'''
def get_letter_count(somestring):
    '''get individual letters in each string'''
    temp_alph = {}
    for letter in somestring:
        if letter in temp_alph.keys():
            temp_alph[letter] = temp_alph[letter] + 1
        else:
            temp_alph[letter] = 1
    return temp_alph

def number_needed(str1, str2):
    '''given two strings determine if they are anagrams'''
    total = 0
    temp_alph1 = get_letter_count(str1)
    temp_alph2 = get_letter_count(str2)

    for each in temp_alph1.keys():
        if each in temp_alph2.keys():
            if temp_alph1[each] > temp_alph2[each]:
                difference = temp_alph1[each] - temp_alph2[each]
                total = total + difference
        elif each not in temp_alph2.keys():
            total = total + temp_alph1[each]
    
    for each in temp_alph2.keys():
        if each in temp_alph1.keys():
            if temp_alph2[each] > temp_alph1[each]:
                diff = temp_alph2[each] - temp_alph1[each]
                total = total + diff
        elif each not in temp_alph1.keys():
            total = total + temp_alph2[each]
    return total


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)





###################3

def get_letter_count(somestring):
    '''get individual letters in each string'''
    temp_alph = {}
    for letter in somestring:
        if letter in temp_alph.keys():
            temp_alph[letter] = temp_alph[letter] + 1
        else:
            temp_alph[letter] = 1
    return temp_alph

def number_needed(str1, str2):
    total = 0
    temp_alph1 = get_letter_count(str1)
    temp_alph2 = get_letter_count(str2)

    for each in temp_alph1.keys():
        if each in temp_alph2.keys():
            if temp_alph1[each] > temp_alph2[each]:
                difference = temp_alph1[each] - temp_alph2[each]
                total = total + difference
        elif each not in temp_alph2.keys():
            total = total + temp_alph1[each]
    
    for each in temp_alph2.keys():
        if each in temp_alph1.keys():
            if temp_alph2[each] > temp_alph1[each]:
                diff = temp_alph2[each] - temp_alph1[each]
                total = total + diff
        elif each not in temp_alph1.keys():
            total = total + temp_alph2[each]
    return total

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)




