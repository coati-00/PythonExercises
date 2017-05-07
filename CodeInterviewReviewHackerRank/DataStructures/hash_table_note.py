'''After reading Python docss --> Counter is a data type that is a dictionary
but counts duplicate elements'''
from collections import Counter


def ransom_note_as_list(magazine, ransom):
    '''determine if ransom note can be constructed from words in magazine'''
    if len(ransom) > len(magazine):
        print "note is longer than magazine list"
        return False
    '''if there are more words in the ransom note than the magazine,
    cannot be done'''
    
    for word in ransom:
        if word not in magazine:
            #print "word " + word + " missing from magazine" 
            return False
        if word in magazine:
            #print magazine
            rmword = magazine.index(word)
            del magazine[rmword]
            #magazine = magazine.pop(rmword)
            print magazine
    return True

def get_word_count(somelist):
    '''get individual letters in each string'''
    temp_alph = {}
    for word in somelist:
        if word in temp_alph.keys():
            temp_alph[word] = temp_alph[word] + 1
        else:
            temp_alph[word] = 1
    return temp_alph

def ransom_note_dict(magazine, ransom):
    '''guess as instructions indicate should probably be solved as a dict'''
    if len(ransom) > len(magazine):
        '''if there are more words in the ransom note than the magazine,
        cannot be done'''
        return False
    
    temp_magazine = get_word_count(magazine)
    temp_note = get_word_count(ransom)

    '''For each word in the note, check to see if it is in the magazine'''
    for each in temp_note.keys():
        if each in temp_magazine.keys():
            '''if the note uses more of one word than the magazine contains'''
            if temp_note[each] > temp_magazine[each]:
                return False
        elif each not in temp_magazine.keys():
            return False

    return True


def ransom_note(magazine, ransom):
    # result = Counter(magazine) - Counter(ransom)
    print (Counter(ransom) - Counter(magazine)) == {}
    return (Counter(ransom) - Counter(magazine)) == {}

#m, n = map(int, raw_input().strip().split(' '))
#magazine = raw_input().strip().split(' ')
#ransom = raw_input().strip().split(' ')

magazine = ['we', 'go', 'home', 'now', 'now', 'Now']
ransom = ['now', 'now', 'now', 'now']
# ransom = ['we', 'go', 'home', 'now']
#ransom = ['we', 'go', 'home', 'now', 'Now']
#ransom = ['we', 'go', 'home', 'soon']
#ransom = ['go', 'home', 'soon']
#ransom = ['go', 'home', 'home']
#ransom = ['home', 'home', 'home']
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
