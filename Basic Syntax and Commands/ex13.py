# MODULES or LIBRARY

from sys import argv

script, first, second, third = argv # give value provided to variables

print('The script is called :', script)
print('Your first variable is :', first)
print('Your second variable is :', second)
print('Your third variable is :', third)



''' OUTPUT
python3 /home/madhur3u/Desktop/Python3/ex13.py 1 2 3
The script is called : /home/madhur3u/Desktop/Python3/ex13.py
Your first variable is : 1
Your second variable is : 2
Your third variable is : 3
'''

a = int(input ('Enter a number')) # convert string to int for operation
print('The square of your number is', a*a)

# The argv is the ”argument variable,” a very standard name in programming that you will find used in
# many other languages. This variable holds the arguments you pass to your Python script when you run
# it.

# This program can be used when we need to provide the variables while executing and not inside the
# script. The 1st arg will always give script and other the variables.

# The command line inputs are always string
