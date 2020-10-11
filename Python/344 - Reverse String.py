"""
Topics: | Two Pointers | String |
"""

class Solution:
    
    # Iterative method
    def reverseString(self, string):
        """
        Time:  O(n)
        Space: O(1)        
        """
        i, j = 0, len(string) - 1
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        
#     # Recursive method
#     def reverseString(self, string):
#         """
#         Time:  O(n)
#         Space: O(n)
#         """
#        
#         def helper(start, end):
#             if start < end:
#                 string[start], string[end] = string[end], string[start]
#                 helper(start + 1, end - 1)   
#
#         helper(0, len(string) - 1)
        