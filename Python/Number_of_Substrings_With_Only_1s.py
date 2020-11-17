# Leetcode problem link: https://leetcode.com/problems/number-of-substrings-with-only-1s/submissions/

# Problem:
# Given a binary string s (a string consisting only of '0' and '1's).
# Return the number of substrings with all characters 1's.
# Since the answer may be too large, return it modulo 10^9 + 7.
# (For convenience we say |s| = n)

# Attempts
# A naive attempt would be to go through all possible substrings,
# then for each substring, check whether it consists of all '1's.
# This will take O(n^3) time, which is not ideal...

# Solution
# An efficient way to solve this is to keep track of
# the running total of consecutive ones
# then add the corresponding number of subtrings with only '1's
# to the total.

# The way to do this is to 'break down' the string
# at the '0's, then count the number of '1's in the string
# and add the corresponding triangular number to our answer.
# (Exercise: Prove '1...1' with k '1's has k(k+1)/2 required substrings.)

# e.g. for '1100111' -> 11|0|0|111
# The first two characters are '1's, but the third is '0'.
# We note that there are 2 consecutive '1's then a '0',
# hence this contributes to 2*(2+1)/2 = 3 to our answer.
# The next '0' occurs immediately, so nothing is added.
# We then reach the end of the input before finding another '0',
# where we pass through 3 '1's. This adds 3*(3+1)/2 = 6 to the result.
# So our answer is 9.

class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        t = 0
        for c in s:
            if c=="1":
                t += 1
            else:
                count += t*(t+1)//2
                t = 0
        count += t*(t+1)//2
        return count%(10**9+7)  # as required in description