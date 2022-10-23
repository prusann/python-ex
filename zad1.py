def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

def is_numberic(x,y):
    if x or y == float:
        raise ValueError('Bad type of arguments')
