'''
Link: https://leetcode.com/problems/regular-expression-matching/

10. Regular Expression Matching (Hard)

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(re.findall(p,s))==0:
            return False
        if re.findall(p,s)[0]==s:
            return True
        else:
            return False
