# Find the smallest positive missing number in unsorted array

# Note that we are not considering the integer 0 while finding the smallest positive number. We will start searching from integer 1. 

array = [ 2, 1, -5, 4, -3, 1, -3, 4, -1 ]
for index in range ( 0 , len ( array ) ) :
    if array.count ( index + 1 ) == 0 :
        print ( index + 1 )
        break
