format1='{} {} {} {}'

print(format1.format(1,2,3,4))
print(format1.format(1,2,3,4,5))
print(format1.format('hi','hello','bye','sayonara'))
print(format1.format(True, False, False, True))

'''
This is being used as a function
format1 is just a string which can get 4 variables denoted by {}
when we use format1.format() we are telling the pc to use the given inputs inside
brackets as it is in format 1

print(format1.format(1,2,3,4,5))
here the 5th will not be printed as it can only take 4 variables

we xan also use anything in between the brackets in format1 and it will reflect
in every output

format1='{} : {} : {} : {}' #like this
'''
