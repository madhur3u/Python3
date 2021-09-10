'''
Write an efficient algorithm to replace every element of a given array with the least greater 
element on its right or with -1 if there are no greater element.
Topic: Array
Time: O(n^2)
Space: 0(1)
Input: (10,100,93,32,35,65,80,90,94,6) Output: (32,-1,94,35,65,80,90,94,-1,-1)'''

a = list(map(int, input().split()))
l = len(a)
x = -1
i = 0
max2 = max(a[i:l])
while i < l - 1 :
    max2 = max(a[i:l])
    temp = max2
    
    for j in range(i+1,l):
        if a[j] > a[i] and a[j] < max2 : max2 = a[j]

    
    if max2 == temp and max2 <= a[i] : a[i] = x
    else : a[i] = max2
    i += 1

a[i] = x
print(a)
    
