# RETURN FROM A FN

def add(a,b):
    print(f'Adding {a} and {b} ')
    return a+b      # returning a value

def subt(a,b):
    print(f'Subtracting {a} and {b} ')
    return a-b

def multiply(a,b):
    print(f'Multiplying {a} and {b} ')
    return a*b

def divide(a,b):
    print(f'Dividing {a} and {b} ')
    return a/b

w = add(10,5)       # assigning the return value to a variable
print(w)
x = subt(45,15)
print(x)
y = multiply(9,9)
print(y)
z = divide(42,5)
print(z)

print() # just to print an ENTER

temp = add(w, subt(x, multiply(y, divide(z,2)))) #in this 1st the inner fn divide will work then multiply and so on...
print('\nNow what was this ? ', temp)
