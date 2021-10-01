# https://my.newtonschool.co/playground/code/u6rmk1bhiwps/

# You are given a two dimensional matrix with N rows and M columns. Each cell (i, j) of the matrix has some value denoted by Ai,j.
# You can do some operations on the matrix (possibly many or zero). In a single operation, you can choose any two adjacent cells 
# and increment the value of each of them by 1. Find the minimum number of operations to make the values of all the cells of the 
# matrix equal. If it's not possible to make all cells equal print -1.

# Constraints:
# 1 ≤ N, M ≤ 50
# -10**9 ≤ Ai,j ≤ 10**9

n, m = map(int, input().split())				# input row and col
a = []											# array to form

max_num = -10**9								# we find max in 2d array, so keeping it minimum possible initially

for i in range(n):
	a.append(list(map(int, input().split())))	# input 2d array
	max_num = max(max_num, max(a[i]))			# finding max for each row, and then comparing it with max


# we need to find number of operations needed to make all element equal
# a operations is increment any two adjacent cells
# so we will found the max value in array 1st
# now we will try to make all values equal to max
# take two adjacent cells and check if they are less than max
# if they are, find the difference between max and both and take minimum
# minimum as we are going to add the difference and we dont want any element to be > max
# so add difference to elements
# the diff will be equal to no. of operations so add that also   
operations = 0
flag = True

for i in range(n):
	for j in range(m):

		if  (j != m - 1) and (a[i][j] < max_num) and (a[i][j+1] < max_num) :	# checking with adjacent right row
	
			diff = min ((max_num - a[i][j]),(max_num - a[i][j+1]))
			a[i][j] += diff
			a[i][j+1] += diff

			operations += diff

		if  (i != n - 1) and (a[i][j] < max_num) and (a[i+1][j] < max_num):		# checking with adjacent bottom row
    			
			diff = min ((max_num - a[i][j]),(max_num - a[i+1][j]))
			a[i][j] += diff
			a[i+1][j] += diff

			operations += diff

	# by the time one row operation is complete that row should have 
	# all elements equal, if it do not have that it means we cannot
	# make all elements equal, so we check this here, sum of each row
	# will be comapred with maxnum * no of col and they should be equal  
	if sum(a[i]) != max_num * m:
    		
		flag = False
		break

# for printing no. of operations
if flag == True : 
	print(operations)
else : 
	print(-1)

# for printing the updated matrix
if flag == True : 
	for i in range(n): print(*a[i])
