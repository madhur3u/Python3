# https://my.newtonschool.co/playground/code/iixoz20umvl5/

# Given a positive integer N, we define the set AN as {1, 2, 3, ... N-1, N}.
# Find the size of the largest subset of AN, such that if x belongs to the subset, then 2x does not belong to the subset.

t = int(input())

for i in range(t):			# test cases
    	
	N = int(input())		# N, till which we need to find the largest subset {1,2,3,....,N}
	ans = 0					# this holds the answer


	# run the loop till N = 0
	# take half of the numbers in N this will give us all odd numbers
	# as odd numbers can never be 2*x so we can take all odd numbers
	# inc ans by 1 if our N was odd as we do floor division so that odd number was not considered
	# now update N to -> N // 4, this is done to take those even numbers which are not considered  
	while N :
    	
		ans = ans + N // 2 

		if N % 2 != 0 : 
			ans += 1
		
		N = N // 4

	print(ans)

#########################################################################################################

# code for if we need to print the subset 
# Given a positive integer N, we define the set AN as {1, 2, 3, ... N-1, N}.
# Find the largest subset of AN, such that if x belongs to the subset, then 2x does not belong to the subset.

def print_subset(N):
	ans = []
	c = 0

	# our set will have number from 1 to N so we need to find a subset
	# in which if there is a number x then there should not be 2*x
	# so first we can say that all odd numbers will be part of set
	# as they are not divisible by 2
	# next we can have those even numbers which are ans[c] * 4
	# this way we will never take 2 * x numbers  
	for num in range(1, N + 1):
		
		if num % 2 != 0:
			ans.append(num)             # taking all odd
		
		else :
			if num == ans[c] * 4 :      # even which are multiple of 4 of the numbers
				ans.append(num)         # already present in the answer array
				c += 1                  # inc c to check for next number in ans array

	print(*ans)

