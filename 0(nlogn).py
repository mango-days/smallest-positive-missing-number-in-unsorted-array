# Find the smallest positive missing number in unsorted array

# Note that we are not considering the integer 0 while finding the smallest positive number. We will start searching from integer 1. 

ans = [ 2, 1, -5, 4, -3, 1, -3, 4, -1 ]
ans.sort()
check = 1
for index in range ( 0 , len ( ans ) ) :
    print ( check , ans [ index ] )
    if check == ans [ index ]  : check += 1
print ( check )