def add(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

def subtract(*args):
    difference = args[0]
    for each in args:
        difference = difference - each
    return difference

def multiply(*args):
    multiply = 1
    for each in args:
        multiply *= each
    return multiply

print(add[2, 3, 1, 2])