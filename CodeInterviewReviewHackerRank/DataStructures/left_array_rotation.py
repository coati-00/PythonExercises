'''
For an array of n elements write a function that shifts each of the elements to the left. Input is the number of times to move the elements one rotation.

https://www.hackerrank.com/challenges/ctci-array-left-rotation
'''

def rotate_one_left(a, n):
    new_array = []
    temp = a[0]
    counter = 1
    while counter < n:
        new_array.append(a[counter])
        counter = counter + 1
    new_array.append(a[0])
    return new_array

def array_left_rotation(a, n, k):
    counter = 0
    new_array = a
    while counter < k:
        new_array = rotate_one_left(new_array, n)
        counter = counter + 1
    return new_array


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

