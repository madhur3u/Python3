# Given an array of Int find min product among all triplets combinations

a = list(map(int, input().split()))
a.sort()
p1 = a[0]*a[1]*a[2]
p2 = a[0]*a[-1]*a[-2]
print(min(p1,p2))

# O(n) approach without using sort            https://www.techiedelight.com/find-minimum-product-triplets-array/

    first = A[0]
    second = sys.maxsize
    third = sys.maxsize
 
    for i in range(1, len(A)):
 
        # if the current element is less than the smallest element found so far
        if A[i] < first:
            third = second
            second = first
            first = A[i]
 
        # if the current element is less than the second smallest element
        elif A[i] < second:
            third = second
            second = A[i]
 
        # if the current element is less than the third smallest element
        elif A[i] < third:
            third = A[i]
 
    # 2. Find the largest and second largest element in the list
    max1 = A[0]
    max2 = -sys.maxsize
 
    for i in range(1, len(A)):
 
        # if the current element is more than the largest element found so far
        if A[i] > max1:
            max2 = max1
            max1 = A[i]
 
        # if the current element is more than the second largest element
        elif A[i] > max2:
            max2 = A[i]
 
    return min(first * second * third, max1 * max2 * first)
