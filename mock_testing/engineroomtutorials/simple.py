def add_and_multiply(x, y):
    addition = x + y
    multiple = multiply(x, y)
    return (addition, multiple)

def multiply(x, y):
    '''assume inner function outside contol changes'''
    return x * y + 3

def orig_multiply(x, y):
    return x * y
