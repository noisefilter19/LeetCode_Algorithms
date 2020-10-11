## Description 

# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

# In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

# Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

## Examples

# Example 1:


# Input: n = 3
# Output: 2
# Explanation: arr = [1, 3, 5]
# First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
# In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].


## Explanation 


# As Elements of the the array are odd numbers 

# The minimum operations are when all the elements are equal to n. This is more on observation.

# case 1 : Number of elements are even numbers .
# n = 6 ; [1,3,5,7,9,11] As u observe number of operations are like 1 , 3 ... , 2*(n/2)-1 
# Add all of them to get the answer . 1 + 3 + ... + 2*(n/2)-1 = ((n/2)**2)


# case 2 : Number of elements are odd numbers .
# n = 5 ; [1,3,5,7,9] As u observe number of operations are like 2 , 4 ... , 2*(n/2)
# Add all of them to get the answer . 2 + 4 + ... + 2*(n/2) = ((n-1)*(n+1)/4))



## Code

```
class Solution:
    def minOperations(self, n: int) -> int:
        if n%2 ==0:
            return int((n/2)**2)
        else:
            return int(((n-1)*(n+1)/4))
            
 ```

