# if else statement in PYTHON

a = 2
b = 3

if a > b :
    print(a)
else :
    print(b)

# condition inside else-if should give true or false only
a += 1 # this means a = a + 1

if a > b :
    print(a)
elif a == b :
    print('equal')
else :
    print(b)

# What happens if multiple elif blocks are True ? Python starts at the top and
# runs the first block that is True , so it will run only the first one.
x = 10
print(x in range(10)) # x in range(10) checks if x lie between 0 - 9 (n-1)
print(5 < x < 15) # other way to check, here it checks if x lie between 5 and 15

if(5 < x < 15) : print('Yessssssss')
