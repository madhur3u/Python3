# WHILE LOOPS

numbers = []

i = 0
while i < 6 :
    numbers.append(i)
    i+=1
print(numbers)

def counting (n) :
    i = 1
    a = []
    while i <= n :
        a.append(i)
        i+=1
    return a

print('Enter till which value you want to count')
m = int(input())
print(counting(m))
