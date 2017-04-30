def ransom_note(magazine, ransom):
    '''determine if ransom note can be constructed from words in magazine'''
    ransom_words = ransom.split()
    magazine_words = magazine.split()
    if len(ransom_words) > len(magazine_words):
        print "note is longer than magazine list"
        return False
    '''if there are more words in the ransome note than the magazine,
    cannot be done'''
    
    for word in randsom_words:
        if word not in magazine_words:
            print "word " + word + " missing from magazine" 
            return False
    return True
            

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"