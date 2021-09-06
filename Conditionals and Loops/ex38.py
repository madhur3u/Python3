a = '1 2 3 4 5'
list1 = a.split(' ')
a1 = '6 7 8 9 10 11 12 13 14 15'
list2 = a1.split(' ')

# take elements from list 2 and put in list 1 till list 1 has 10 elements

while len(list1) < 10 : # to take length of a list 
    el = list2.pop(0)
    list1.append(el)

print(list1)
print(list1[1]) # 1st index or 2nd element of list1
print(list1[-1]) # -1 index refers to last index so -2 is 2nd last and so on

print(' '.join(list1)) # will join every element of list using space and print a string
print('$'.join(list1[2:6])) # will join el from index 2 to 5 (n-1)  with $ and print a string

'''
list1 = a.split(' ') -> split the string a whenever it finds space ' ' and store all as a list in list1

len(list1) -> give us no. of elements in list 
el = list2.pop() -> pop out the last element from list2 and store it in el
el = list2.pop(0) -> pop out the first element from list2 and store it in el
list1.append(el) -> add el to the list's next index
'''