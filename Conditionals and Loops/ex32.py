# LISTS AND LOOPS
# Lists are like arrays

numbers = [1, 2, 3, 4, 5] # a list with 5 values
birds = ['owl' , 'sparrow' , 'hoopoe' , 'dove' , 'flycatcher']

# now to print lists we will use FOR LOOPS

for n in numbers :
    print(f'The number is {n}')

for bird in birds :
    print(f'The bird is {bird}')

# the above for loop will run for no. of values the list has and will give the
# 1st value to bird in 1st iteration and so on...

elements = []  # making list from user

for i in range (0,6) :
    print(f'adding {i} to the list')
    elements.append(i)  # append will add the value of i to the list elements

print(elements) # will print list like this [0, 1, 2, 3, 4, 5]
