'''
Given the three types of string edits - insert a character, remove a character, or replace a character, create
a function to determine if 2 strings are one edit or zero edits away from each other.

'''


teststr1 = 'pale'
teststr2 = 'ple'
teststr3 = 'pales'
teststr4 = 'bale'
teststr5 = 'bae'



def replace_one(str1, str2):
    diff_letter = False
    counter = 0
    while counter < len(str1):
        if str1[counter] != str2[counter]:
            if diff_letter:
                return False
            diff_letter = True
        counter = counter + 1
    return True


# replace_one(teststr1, teststr4)
# replace_one(teststr2, teststr5)


def insert_one(str1, str2):
    counter_one = 0
    counter_two = 0
    while (counter_two < len(str2)) and (counter_one < len(str1)):
        if str1[counter_one] != str2[counter_two]:
            print "str1[counter_one]  " + str(str1[counter_one])
            print "str2[counter_two]  " + str(str2[counter_two])
            #print "counter_one  " + str(counter_one)
            #print "counter_two  " + str(counter_two)
            if counter_one != counter_two:
                print "false"
                return False
            counter_two = counter_two + 1
        else:
            counter_one = counter_one + 1
            counter_two = counter_two + 1
    print "true"
    return True

#insert_one(teststr1, teststr2) # false
#insert_one(teststr1, teststr3) # true
#insert_one(teststr3, teststr2) # false
#insert_one(teststr4, teststr5) # true


def one_edit_away(str1, str2):
    if (len(str1) == len(str2)):
        return replace_one(str1, str2)
    elif (len(str1) + 1 == len(str2)):
        return insert_one(str1, str2)
    elif (len(str1) - 1 == len(str2)):
        return insert_one(str2, str1)



one_edit_away(teststr1, teststr2)
one_edit_away(teststr1, teststr3)
one_edit_away(teststr2, teststr3)
one_edit_away(teststr4, teststr5)
one_edit_away(teststr1, teststr4)
one_edit_away(teststr2, teststr5)