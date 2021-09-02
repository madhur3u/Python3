#escape sequences
'''
print('my height is 6'5"')
#above wil give error as the quote after 6 will act like string end

print("my height is 6'5"") #same here

#we can use \ before the quote which we dont want to be as end of string
'''

print('my height is 5\'10"')

#can also be done using triple quotes
print('''my height is 5'10" ''')
print('\n\n\n') #leave 3 lines

a='Hello this line will \nsplit' #after \n to new line
b='\nto print slash use double slash \\ \n'
c='\tthis will tab'
print(a,b,c)

#list using tab
print('\n\n')

print('''List of birds around me
\t*Sparrow
\t*Myna
\t*Pigeon
\t*Dove''')
