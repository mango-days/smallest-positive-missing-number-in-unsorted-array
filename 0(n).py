# Find the smallest positive missing number in unsorted array

# Note that we are not considering the integer 0 while finding the smallest positive number. We will start searching from integer 1. 

numbers = [ 2, 1, -5, 4, -3, 1, -3, 4, -1 ]
index2 = len ( numbers ) - 1
index1 = 0

while index1 < index2 :
    if numbers [ index1 ] < 0 : index1 += 1
    elif numbers [ index2 ] > 0 : index2 -= 1
    elif ( numbers [ index1 ] > 0 and numbers [ index2 ] < 0 ) :
        temp = numbers [ index1 ] 
        numbers [ index1 ] = numbers [ index2 ] 
        numbers [ index2 ] = temp
        index1 += 1
        index2 -= 1
        
ans = numbers [ index1 : ]

check = 1
for index in range ( 0 , len ( ans ) ) :
    if check == ans [ index ] : check += 1
print ( check )
