# https://www.hackerrank.com/challenges/collections-counter/problem

# shoe shop owner. His shop has number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are number of customers who are willing to pay 'money' amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money earned.
# 10                            no. of shoes
# 2 3 4 5 6 8 7 6 5 18          size
# 6                             customers no.
# 6 55                          shoe size and money
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50


from collections import Counter             # A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

n = int(input())
a = list(map(int, input().split()))
dsize = Counter(a)                          # making a dictionary from input array, size of shoes as keys and their count as values
total = 0                                   # total money req

for i in range(int(input())):               # no. of customers
    
    size, money = map(int, input().split()) 
    
    if (size in dsize) and (dsize[size] > 0):   # checking if shoe size is present, and if present, do we have it
        
        total += money                      # add money if availiable
        dsize[size] -= 1                    # decrease the value as it is sold

print(total)
            
