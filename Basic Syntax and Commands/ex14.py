from sys import argv

script, name = argv
prompt = '>>\t '

print(f'\nHi {name} you are working on {script} script')
print('\nAnswer the following questions')
print('What is your age')
age = input(prompt)

print('No. of birds seen')
nbird = input(prompt)

print('What was the most common bird seen today')
cbird = input(prompt)

print(f'''\n
Hello {name} so you are {age} years old
You saw {nbird} birds today
And the most common bird was {cbird}
'''
)

# We make a variable prompt that is set to the prompt we want, and we give that to input instead of
# typing it over and over. Now if we want to make the prompt something else, we just change it in this
# one spot and rerun the script.
