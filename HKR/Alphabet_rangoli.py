# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

n = int(input())                                    # input

w = (2*n - 1) + (2*n - 2)                           # width of a row
val = chr(96+n)                                     # this will give us 1st character of the row

print(val.center(w,'-'))                            # 1st line, use for corner case n = 1


# now we will print 1st half from 2nd line till nth line
# make a string for each row and each row will iterate from 0 to i
# string will add the character -j to decrease in each iteration
# when we come out of inner loop we will have j-i-h-g- half character line
# so reverse the string and add from 3 to avoid repitition
# now print using center
for i in range(2,n+1):

    string = ''

    for j in range(i):
        string = string + chr(96 + n - j) + '-'         # this will make our half string row

    string = string + string[::-1][3:]                  # this is adding other half by reversing
    print(string.center(w,'-'))                         # print with center

# for the 2nd half itrate i in reverse and done
for i in range(n-1,0,-1):
    
    string = ''

    for j in range(i):
        string = string + chr(96 + n - j) + '-'

    string = string + string[::-1][3:]
    print(string.center(w,'-'))

'''

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

'''
