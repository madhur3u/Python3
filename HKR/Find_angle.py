# We can Solve this problem by using a property: ** That a median on the hypotenuse 
# divides the right angled triangle in two isoceles triangle. ( as it form circle's radius)** * Means AM=BM=CM * 
# So, angle(MBC) = angle(MCB)
# Now find angle(MCB) [You can use 'tan' ] as perpendicular and base is given

import math

p = int(input())
b = int(input())

print(str(round(math.degrees(math.atan(p/b)))) + chr(176))  # chr 176 is for degrees, atan for tan**-1
