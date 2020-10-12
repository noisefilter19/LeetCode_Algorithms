# Palindromic Substrings
# Problem link: https://leetcode.com/problems/palindromic-substrings/
# 
# Given a string, your task is to count how many palindromic substrings in this string.
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

'''
    Approach
    Iterate through the string character by character
    While iterating, check all the palindromes from the current character till the end
'''

class Solution:
    def isPalindrome(self, sub_s: str) -> bool:
        return sub_s == sub_s[::-1]
    
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        for index in range(len(s)):
            for sub_index in range(index+1, len(s)):
                if self.isPalindrome(s[index:sub_index+1]):
                    count += 1
        return count
