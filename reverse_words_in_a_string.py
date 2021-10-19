#problem-link: https://leetcode.com/problems/reverse-words-in-a-string/

'''
Problem Description:

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        
        sList = list(map(str, s.split()))
        revList = sList[::-1] 
        rev = " ".join(s for s in revList)
        return rev
