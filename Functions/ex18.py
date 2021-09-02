# FUNCTIONS
# create a function by using the word def in Python

def print_two(*args): # this work like how we use argv in script
    arg1, arg2 = args # providing value input by users to variables
    print(arg1,arg2)

# indent all lines of code you want in the function four spaces

def print_two_2(arg1, arg2): # we can directly use variable by user like this
    print(arg1,arg2)         # this is netter than above

def print_one(arg1):
    print(arg1)

def print_none():                       # FUNCTION DEFINING
    print('I will print only this')

print_two('Adachi ','Shimamura')
print_two_2('Hello ','How are you')
print_one('India')
print_none()                            # CALLING A FUNCTION
