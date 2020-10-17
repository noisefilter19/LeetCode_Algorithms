# LeetCode Problem link - https://leetcode.com/problems/longest-palindromic-substring/

#The solution is to find the Longest Palindrome
class Solution:
    def longestPalindrome(self, string): 
        maxLength = 1

        start = 0
        leng = len(string) 

        low = 0
        high = 0

        for i in range(1, leng):  
            low = i - 1
            high = i 
            while low >= 0 and high < leng and string[low] == string[high]: 
                if high - low + 1 > maxLength: 
                    start = low 
                    maxLength = high - low + 1
                low -= 1
                high += 1

            low = i - 1
            high = i + 1
            while low >= 0 and high < leng and string[low] == string[high]: 
                if high - low + 1 > maxLength: 
                    start = low 
                    maxLength = high - low + 1
                low -= 1
                high += 1

        return(string[start:start + maxLength])
