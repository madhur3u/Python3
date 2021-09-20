# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = list(map(int, input().split()))

arr = list(set(arr))      # convert list to set to remove repeated elements and the convert again to list
arr.sort()                # sort the list
print(arr[-2])            # print the 2nd last element
