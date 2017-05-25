'''
Implement a basic string compression using the counts of repeated characters.
E.g. aabcccccaaa would become a2b1c5a3

If the compressed string would not be any shorter than the original - if all letter are 1 or 2 for example,
simply return the original string...

'''

def compress_string(somestring):
    compressed_string = ""
    count_consecutive = 0
    counter = 0
    while counter < len(somestring):
        count_consecutive = count_consecutive + 1

        # check to see if the next character is different than the one currently
        # being examined, if it is append it to the result string
        if counter + 1 >= len(somestring) or somestring[counter] != somestring[counter + 1]:
            compressed_string = compressed_string + somestring[counter] + str(count_consecutive)
            count_consecutive = 0
        counter = counter + 1
    if len(compressed_string) < len(somestring):
        return compressed_string
    else:
        return somestring

print compress_string("aabcccccaaa")
print compress_string("aabccaa")
print compress_string("aaaabbbbcccccaaa")