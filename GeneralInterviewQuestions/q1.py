'''given an array with 3 strings a b c 4 strigns b c d e find intersection of arrays'''

arr1 = ['a','b','c']
arr2 = ['b','c','d', 'e']


def count_elements(somestring):
    temp_elem = {}
    for each in somestring:
        if each in temp_elem:
            temp_elem[each] = temp_elem[each] + 1
        if each not in temp_elem:
            temp_elem[each] = 1
    return temp_elem

def order_length(arr1, arr2):
    first = {}
    second = {}
    if len(arr1) < len(arr2):
        return arr1, arr2


def get_same_elements_dict(arr1 , arr2):
    #go over shorter one first
    first = count_elements(arr1)
    second = count_elements(arr2)
    same = []
    for elem in first.iterkeys():
        if second.has_key(elem):
            same.append(elem)
    print same
    return same


def get_same_elements(arr1 , arr2):
    #go over shorter one first
    same = []
    for elem in arr1:
        if elem in arr2:
            same.append(elem)
    print same
    return same

get_same_elements_dict(arr1, arr2)