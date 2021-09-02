# The variables in your function are not connected to the variables in your script
# We can also call a fn inside a fn

def park(n1, n2):
    print(f'The park has {n1} dogs')
    print(f'The park has {n2} birds')
    print(f'The park has {n1+n2} animals')
    print('Thanks for visiting our park\n')

# we can give arguments in many ways
# 1. DIRECTLY
park(5,10)

# 2. BY USING VARIABLES
dog = 10
bird = 20
park(dog,bird)

# 3. WECAN DO MATHS INSIDE arguments
park(2*2, 3+9)

# 4. WE CAN USE BOTH VARIABLES AND VALUES
park(dog+10, bird*2)

'''OUTPUT

~/Desktop/Python3$ python3 ex19.py
The park has 5 dogs
The park has 10 birds
The park has 15 animals
Thanks for visiting our park

The park has 10 dogs
The park has 20 birds
The park has 30 animals
Thanks for visiting our park

The park has 4 dogs
The park has 12 birds
The park has 16 animals
Thanks for visiting our park

The park has 20 dogs
The park has 40 birds
The park has 60 animals
Thanks for visiting our park
'''
