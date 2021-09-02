zoo_capacity=100
bird=52
deer=13
lion=2
snakes=17

total_animals = bird + deer + lion + snakes
capacity_left = zoo_capacity - total_animals

#now we will see two ways in which we can print the variables

#using the names directly
print('Total mammals= ', deer+lion)
print('Other than mammals= ', total_animals - (deer+lion))

#using format f {}
print(f'Total animals are {total_animals}')
print(f'Capacity of zoo left is {capacity_left}')
