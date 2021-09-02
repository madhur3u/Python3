'''
Taking INPUT

WARNING! We put a end=' ' at the end of each print line. This tells print to not
end the line with a newline character and go to the next line.

'''

print('How many birds are there', end=' ') #so input in same newline
bird = input() #input by user
print('How many animals are there', end=' ')
an = input()
print('Total Population of park is ', bird+an)
#addition result not correct as variables are string
print('\n\n')
'''
since we are not specifying type of input it will always be treated as a string
for int we can use int(input())

'''

#another way of taking INPUT

snake = int(input('Enter no. of snakes ')) #variables are now int
rep = int(input('Enter no. of other reptiles '))
total_rep = snake + rep
print(f'Total reptiles are {total_rep} \n\n')

'''
We can directly ask or prompt people for input by writing the commands in the
() inside the INPUT
'''

name = input('Enter your name\t')
age = input('Enter your age\t')

print(f'\nSo your name is {name} and you are {age} years old')
