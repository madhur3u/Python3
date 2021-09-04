print(
'''\tHello
How are you
Genki desuka
Sayonara'''
)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates # returning 3 vaules


start_point = 10000
beans, jars, crates = secret_formula(start_point) # taking all 3 return values in one line

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # here we are taking 3 values in formula to create a list
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) # list is unpacked using *formula
